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
        raise ValueError("API quotas must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        endpoint = str(item.get("endpoint", "")).strip()
        window = item.get("window_seconds"); requests = item.get("requests"); burst = item.get("burst",0)
        if not endpoint or not isinstance(window,int) or isinstance(window,bool) or window <= 0:
            raise ValueError(f"item {index} has an invalid endpoint or window")
        if requests is None:
            findings.append(Finding("unlimited_requests", "critical", index, f"{endpoint} has no request limit."))
        elif not isinstance(requests,int) or isinstance(requests,bool) or requests <= 0:
            raise ValueError(f"item {index}.requests must be positive or null")
        if item.get("per_client") is not True:
            findings.append(Finding("not_per_client", "high", index, f"{endpoint} is not limited per client."))
        if not isinstance(burst,int) or isinstance(burst,bool) or burst < 0:
            raise ValueError(f"item {index}.burst must be non-negative")
        if burst > 100:
            findings.append(Finding("excessive_burst", "medium", index, f"{endpoint} allows a burst over 100."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (
        ["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class QuotaSentryAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
