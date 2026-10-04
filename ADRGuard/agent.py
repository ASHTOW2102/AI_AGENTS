from __future__ import annotations

import json
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

REQUIRED_SECTIONS = ("context", "decision", "alternatives", "consequences")
VALID_STATUSES = {"proposed", "accepted", "deprecated", "superseded", "rejected"}
PLACEHOLDER = re.compile(r"\b(?:todo|tbd|fixme|xxx)\b|<[^>\n]+>", re.IGNORECASE)
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    location: str
    message: str


@dataclass(frozen=True)
class AuditReport:
    valid: bool
    status: str
    sections: list[str]
    findings: list[Finding]
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _sections(markdown: str) -> dict[str, str]:
    matches = list(HEADING.finditer(markdown))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        name = re.sub(r"[^a-z0-9]+", " ", match.group(1).lower()).strip()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        result[name] = markdown[match.end():end].strip()
    return result


def _status(markdown: str, sections: dict[str, str]) -> str:
    match = re.search(
        r"^(?:status\s*:\s*|[-*]\s*\*\*status\*\*\s*:\s*)([A-Za-z-]+)",
        markdown,
        re.IGNORECASE | re.MULTILINE,
    )
    if match:
        return match.group(1).lower()
    value = sections.get("status", "").splitlines()
    return value[0].strip().lower() if value else ""


def audit_adr(markdown: str, *, source_path: str | None = None) -> AuditReport:
    if not isinstance(markdown, str) or not markdown.strip():
        raise ValueError("ADR content must be non-empty Markdown")

    sections = _sections(markdown)
    status = _status(markdown, sections)
    findings: list[Finding] = []

    if not status:
        findings.append(Finding("missing_status", "high", "status", "ADR status is missing."))
    elif status not in VALID_STATUSES:
        findings.append(
            Finding(
                "invalid_status",
                "high",
                "status",
                f"Unsupported ADR status: {status}.",
            )
        )

    for required in REQUIRED_SECTIONS:
        content = sections.get(required, "")
        if not content:
            findings.append(
                Finding(
                    "missing_section",
                    "high",
                    required,
                    f"Required section '{required.title()}' is missing or empty.",
                )
            )
        elif len(re.sub(r"\s+", " ", content)) < 20:
            findings.append(
                Finding(
                    "thin_section",
                    "medium",
                    required,
                    f"Section '{required.title()}' is too brief to explain the decision.",
                )
            )

    for name, content in sections.items():
        if PLACEHOLDER.search(content):
            findings.append(
                Finding(
                    "unresolved_placeholder",
                    "high" if status == "accepted" else "medium",
                    name,
                    f"Section '{name.title()}' contains unresolved placeholder text.",
                )
            )

    if status == "accepted":
        open_questions = sections.get("open questions", "")
        if open_questions and re.search(r"^\s*[-*]\s+\S", open_questions, re.MULTILINE):
            findings.append(
                Finding(
                    "accepted_with_open_questions",
                    "medium",
                    "open questions",
                    "Accepted ADR still lists unresolved questions.",
                )
            )

    if status == "superseded":
        superseded_text = sections.get("superseded by", "")
        if not superseded_text or not LINK.search(superseded_text):
            findings.append(
                Finding(
                    "missing_supersession_link",
                    "high",
                    "superseded by",
                    "Superseded ADR must link to its replacement.",
                )
            )

    if source_path:
        base = Path(source_path).resolve().parent
        for target in LINK.findall(markdown):
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            local_target = target.split("#", 1)[0]
            if local_target and not (base / local_target).exists():
                findings.append(
                    Finding(
                        "broken_local_link",
                        "medium",
                        target,
                        f"Local link target does not exist: {target}.",
                    )
                )

    codes = {item.code for item in findings}
    recommendations: list[str] = []
    if {"missing_section", "thin_section"} & codes:
        recommendations.append("Document context, the decision, considered alternatives, and consequences.")
    if {"missing_status", "invalid_status"} & codes:
        recommendations.append("Set a lifecycle status: proposed, accepted, rejected, deprecated, or superseded.")
    if "unresolved_placeholder" in codes:
        recommendations.append("Resolve placeholder text before accepting the ADR.")
    if "accepted_with_open_questions" in codes:
        recommendations.append("Resolve or explicitly defer open questions before acceptance.")
    if "missing_supersession_link" in codes:
        recommendations.append("Link superseded records to the replacing ADR.")
    if "broken_local_link" in codes:
        recommendations.append("Repair local ADR links or remove stale references.")

    return AuditReport(
        valid=not findings,
        status=status,
        sections=sorted(sections),
        findings=findings,
        recommendations=recommendations,
    )


class ADRGuardAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model

    def inspect(self, markdown: str, *, source_path: str | None = None) -> AuditReport:
        report = audit_adr(markdown, source_path=source_path)
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report

        try:
            from openai import OpenAI

            safe_payload = {
                "status": report.status,
                "sections": report.sections,
                "findings": [asdict(item) for item in report.findings],
                "recommendations": report.recommendations,
            }
            response = OpenAI().responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                input=(
                    "Explain how to improve this sanitized ADR quality report. "
                    "Do not invent architecture details.\n" + json.dumps(safe_payload)
                ),
            )
            return AuditReport(
                report.valid,
                report.status,
                report.sections,
                report.findings,
                report.recommendations,
                response.output_text.strip(),
                "openai",
            )
        except Exception:
            return report
