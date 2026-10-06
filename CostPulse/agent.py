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
        raise ValueError("services must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        name = str(item.get("name", "")).strip()
        if not name:
            raise ValueError(f"item {index}.name is required")
        values = {}
        for field in ("cost_today", "cost_yesterday", "daily_budget", "untagged_cost"):
            value = item.get(field)
            if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
                raise ValueError(f"item {index}.{field} must be a non-negative number")
            values[field] = float(value)
        if values["cost_today"] > values["daily_budget"]:
            findings.append(Finding("budget_exceeded", "high", index, f"{name} exceeded its daily budget."))
        if values["cost_yesterday"] and values["cost_today"] > values["cost_yesterday"] * 1.5:
            findings.append(Finding("daily_spike", "high", index, f"{name} increased by more than 50 percent day over day."))
        if values["untagged_cost"] > 0:
            findings.append(Finding("untagged_cost", "medium", index, f"{name} contains unallocated spend."))
        if values["cost_today"] and values["untagged_cost"] / values["cost_today"] > 0.2:
            findings.append(Finding("high_untagged_ratio", "high", index, f"{name} has over 20 percent untagged spend."))
    codes = {finding.code for finding in findings}
    recommendations = (
        [f"Review and resolve: {', '.join(sorted(codes))}.", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class CostPulseAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
