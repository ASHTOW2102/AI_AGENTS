"""Secret-safe operational incident triage agent."""

from __future__ import annotations

import json
import os
import re
from dataclasses import asdict, dataclass
from typing import Any

_SECRET_PATTERNS = (
    re.compile(r"(?i)(api[_-]?key|token|password|secret)\s*[:=]\s*[^\s,;]+"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
)
_SEVERITY_TERMS = {
    "critical": ("data loss", "breach", "all users", "production down", "outage"),
    "high": ("payment", "login", "unavailable", "500", "latency", "degraded"),
    "medium": ("error", "failed", "timeout", "incorrect", "bug"),
}


@dataclass(frozen=True)
class TriageReport:
    title: str
    severity: str
    confidence: float
    summary: str
    immediate_actions: list[str]
    investigation_questions: list[str]
    customer_update: str
    redactions: int
    mode: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def redact_secrets(text: str) -> tuple[str, int]:
    """Remove common credential shapes before any model call."""
    redacted = text
    count = 0
    for pattern in _SECRET_PATTERNS:
        redacted, replacements = pattern.subn("[REDACTED]", redacted)
        count += replacements
    return redacted, count


def _severity(text: str) -> tuple[str, float]:
    lowered = text.lower()
    for severity, terms in _SEVERITY_TERMS.items():
        hits = sum(term in lowered for term in terms)
        if hits:
            confidence = min(0.55 + hits * 0.12, 0.95)
            return severity, round(confidence, 2)
    return "low", 0.55


def local_triage(text: str, redactions: int = 0) -> TriageReport:
    severity, confidence = _severity(text)
    first_line = next((line.strip() for line in text.splitlines() if line.strip()), "New incident")
    title = first_line[:77] + ("..." if len(first_line) > 77 else "")
    summary = re.sub(r"\s+", " ", text).strip()[:400]
    return TriageReport(
        title=title,
        severity=severity,
        confidence=confidence,
        summary=summary,
        immediate_actions=[
            "Assign an incident owner and open a timestamped incident log.",
            "Confirm user impact, affected services, and the earliest known failure.",
            "Preserve logs and recent deployment metadata before changing systems.",
            "Mitigate with the safest reversible action; record the result.",
        ],
        investigation_questions=[
            "What changed immediately before the first symptom?",
            "Which regions, tenants, versions, or request paths are affected?",
            "What do service metrics and dependency health show?",
        ],
        customer_update=(
            f"We are investigating a {severity}-priority service issue. "
            "We will share verified impact and the next update time shortly."
        ),
        redactions=redactions,
        mode="local",
    )


def _model_triage(text: str, base: TriageReport) -> TriageReport:
    from openai import OpenAI

    prompt = f"""You are an incident commander. Improve the preliminary report below using
only the supplied incident. Return strict JSON with keys: title, severity, confidence,
summary, immediate_actions, investigation_questions, customer_update.
Severity must be one of critical, high, medium, low. Do not invent facts.
Incident:
{text}

Preliminary report:
{json.dumps(base.to_dict())}
"""
    response = OpenAI().responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        input=prompt,
    )
    raw = response.output_text.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw, flags=re.I)
    payload = json.loads(raw)
    severity = str(payload["severity"]).lower()
    if severity not in {"critical", "high", "medium", "low"}:
        raise ValueError("Model returned an unsupported severity")
    return TriageReport(
        title=str(payload["title"])[:120],
        severity=severity,
        confidence=max(0.0, min(float(payload["confidence"]), 1.0)),
        summary=str(payload["summary"]),
        immediate_actions=[str(item) for item in payload["immediate_actions"]][:8],
        investigation_questions=[str(item) for item in payload["investigation_questions"]][:8],
        customer_update=str(payload["customer_update"]),
        redactions=base.redactions,
        mode="openai",
    )


class IncidentTriageAgent:
    """Triage incidents locally, with an optional model enhancement."""

    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model

    def run(self, incident: str) -> TriageReport:
        if not incident or not incident.strip():
            raise ValueError("Incident description cannot be empty")
        safe_text, redactions = redact_secrets(incident)
        base = local_triage(safe_text, redactions)
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return base
        try:
            return _model_triage(safe_text, base)
        except (KeyError, TypeError, ValueError, json.JSONDecodeError):
            return base
