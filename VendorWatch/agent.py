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
        raise ValueError("vendors must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        name=str(item.get("name","")).strip(); reviewed=item.get("reviewed_days_ago"); alternatives=item.get("alternatives")
        if not name or not isinstance(reviewed,int) or isinstance(reviewed,bool) or reviewed < 0 or not isinstance(alternatives,int) or isinstance(alternatives,bool) or alternatives < 0:
            raise ValueError(f"item {index} has invalid vendor metadata")
        if not str(item.get("owner","")).strip(): findings.append(Finding("missing_owner","high",index,f"{name} has no owner."))
        if reviewed > 365: findings.append(Finding("overdue_review","high",index,f"{name} review is overdue."))
        if item.get("data_agreement") is not True: findings.append(Finding("missing_agreement","high",index,f"{name} lacks a data agreement."))
        if item.get("critical") is True and alternatives == 0: findings.append(Finding("concentration_risk","critical",index,f"{name} is critical with no alternative."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings, len(items), findings, recommendations)

class VendorWatchAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
