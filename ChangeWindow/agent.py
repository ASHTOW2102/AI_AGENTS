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
        raise ValueError("changes must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        change=str(item.get("id","")).strip(); owner=str(item.get("owner","")).strip(); hour=item.get("start_hour"); duration=item.get("duration_minutes")
        if not change or not isinstance(hour,int) or isinstance(hour,bool) or not 0 <= hour <= 23 or not isinstance(duration,int) or isinstance(duration,bool) or duration <= 0:
            raise ValueError(f"item {index} has invalid change metadata")
        if not owner: findings.append(Finding("missing_owner","high",index,f"{change} has no owner."))
        if 9 <= hour < 18: findings.append(Finding("peak_hours","medium",index,f"{change} starts during peak hours."))
        if duration > 120: findings.append(Finding("long_change","medium",index,f"{change} exceeds two hours."))
        if item.get("rollback") is not True: findings.append(Finding("missing_rollback","critical",index,f"{change} has no rollback plan."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings, len(items), findings, recommendations)

class ChangeWindowAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
