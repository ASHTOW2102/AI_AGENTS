from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    item: int
    message: str

@dataclass(frozen=True)
class AuditReport:
    healthy: bool
    items_checked: int
    findings: list[Finding]
    recommendations: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def audit(items: list[dict[str, Any]]) -> AuditReport:
    if not isinstance(items, list) or not items:
        raise ValueError("events must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        level = str(item.get("level", "info")).lower()
        if level in {"error", "critical"}:
            findings.append(Finding("error_event", "high", index, "Error-level event requires investigation."))
        if not str(item.get("request_id", "")).strip():
            findings.append(Finding("missing_request_id", "medium", index, "Event has no request correlation ID."))
        duration = item.get("duration_ms", 0)
        if not isinstance(duration, (int, float)) or isinstance(duration, bool) or duration < 0:
            raise ValueError(f"item {index}.duration_ms must be a non-negative number")
        if duration > 1000:
            findings.append(Finding("slow_event", "medium", index, f"Duration {duration:g}ms exceeds 1000ms."))
        risky = {"password", "token", "secret", "api_key"} & {str(key).lower() for key in item}
        if risky:
            findings.append(Finding("secret_field", "critical", index, "Event contains a secret-like field name."))
    codes = {finding.code for finding in findings}
    recommendations = (
        [f"Review and resolve: {', '.join(sorted(codes))}.", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class LogSentryAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
