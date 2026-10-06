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
        raise ValueError("tickets must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        ticket = str(item.get("id", "")).strip()
        if not ticket:
            raise ValueError(f"item {index}.id is required")
        status = str(item.get("status", "")).lower()
        priority = str(item.get("priority", "")).lower()
        if priority not in {"low", "normal", "high", "urgent"}:
            findings.append(Finding("invalid_priority", "medium", index, f"{ticket} has an unsupported priority."))
        for field in ("age_minutes", "last_update_minutes", "response_sla_minutes"):
            value = item.get(field)
            if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
                raise ValueError(f"item {index}.{field} must be a non-negative number")
        if status not in {"closed", "resolved"} and item["age_minutes"] > item["response_sla_minutes"]:
            findings.append(Finding("response_overdue", "high", index, f"{ticket} exceeded its response SLA."))
        if status not in {"closed", "resolved"} and not str(item.get("owner", "")).strip():
            findings.append(Finding("unowned_ticket", "high", index, f"{ticket} has no owner."))
        if status not in {"closed", "resolved"} and item["last_update_minutes"] > 120:
            findings.append(Finding("stale_update", "medium", index, f"{ticket} has not been updated for over two hours."))
    codes = {finding.code for finding in findings}
    recommendations = (
        [f"Review and resolve: {', '.join(sorted(codes))}.", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class SLAWatchAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
