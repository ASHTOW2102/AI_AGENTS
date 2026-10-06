from __future__ import annotations

import json
import os
import re
from dataclasses import asdict, dataclass
from typing import Any, Iterable

PATTERNS = {
    "email": re.compile(r"(?<![\w.+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![\w.-])", re.I),
    "uk_phone": re.compile(r"(?<!\d)(?:(?:\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3}|(?:\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})(?!\d)"),
    "uk_nino": re.compile(r"(?<![A-Z0-9])(?!(?:BG|GB|KN|NK|NT|TN|ZZ))(?!(?:[DFIQUV][A-Z]|[A-Z][DFIOQUV]))[A-Z]{2}\s?\d{2}\s?\d{2}\s?\d{2}\s?[A-D](?![A-Z0-9])", re.I),
    "uk_postcode": re.compile(r"(?<![A-Z0-9])(?:GIR\s?0AA|[A-Z]{1,2}\d[A-Z\d]?\s?\d[A-Z]{2})(?![A-Z0-9])", re.I),
    "ipv4": re.compile(r"(?<!\d)(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)(?!\d)"),
}
CARD_CANDIDATE = re.compile(r"(?<!\d)(?:\d[ -]?){12,18}\d(?!\d)")

@dataclass(frozen=True)
class Finding:
    kind: str
    count: int
    samples: list[str]

@dataclass(frozen=True)
class PrivacyReport:
    safe: bool
    findings: list[Finding]
    total_matches: int
    redacted: str
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def _luhn(value: str) -> bool:
    digits = [int(x) for x in re.sub(r"\D", "", value)]
    if not 13 <= len(digits) <= 19:
        return False
    total = 0
    parity = len(digits) % 2
    for index, digit in enumerate(digits):
        if index % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0

def _mask(value: str) -> str:
    visible = re.sub(r"\s+", "", value)
    return f"<redacted:{len(visible)}>"

def _matches(text: str) -> dict[str, list[str]]:
    found = {kind: [m.group(0) for m in pattern.finditer(text)] for kind, pattern in PATTERNS.items()}
    found["payment_card"] = [m.group(0) for m in CARD_CANDIDATE.finditer(text) if _luhn(m.group(0))]
    return {kind: values for kind, values in found.items() if values}

def _redact(text: str) -> str:
    spans: list[tuple[int, int]] = []
    for pattern in PATTERNS.values():
        spans.extend((m.start(), m.end()) for m in pattern.finditer(text))
    spans.extend((m.start(), m.end()) for m in CARD_CANDIDATE.finditer(text) if _luhn(m.group(0)))
    for start, end in sorted(spans, reverse=True):
        text = text[:start] + _mask(text[start:end]) + text[end:]
    return text

def scan_text(text: str) -> PrivacyReport:
    if not isinstance(text, str) or not text:
        raise ValueError("text must be a non-empty string")
    matches = _matches(text)
    findings = [
        Finding(kind, len(values), sorted({_mask(value) for value in values})[:3])
        for kind, values in sorted(matches.items())
    ]
    total = sum(item.count for item in findings)
    recommendations = (
        ["Replace detected identifiers with approved tokens before sharing.", "Review false positives before deleting or changing source data."]
        if total else ["No supported personal-data patterns were detected."]
    )
    return PrivacyReport(total == 0, findings, total, _redact(text), recommendations)

def redact_json(value: Any) -> Any:
    if isinstance(value, str):
        return _redact(value)
    if isinstance(value, list):
        return [redact_json(item) for item in value]
    if isinstance(value, dict):
        return {key: redact_json(item) for key, item in value.items()}
    return value

class PIIGuardAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model

    def inspect(self, text: str) -> PrivacyReport:
        report = scan_text(text)
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report
        try:
            from openai import OpenAI
            safe = {"findings": [asdict(item) for item in report.findings], "total_matches": report.total_matches}
            response = OpenAI().responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                input="Explain this sanitized PII scan and suggest safe handling. Never reconstruct identifiers.\n" + json.dumps(safe),
            )
            return PrivacyReport(report.safe, report.findings, report.total_matches, report.redacted, report.recommendations, response.output_text.strip(), "openai")
        except Exception:
            return report
