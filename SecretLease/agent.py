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
        raise ValueError("secrets must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        name = str(item.get("name", "")).strip()
        owner = str(item.get("owner", "")).strip()
        age = item.get("age_days"); rotation = item.get("rotation_days")
        if not name or not isinstance(age,int) or isinstance(age,bool) or age < 0 or not isinstance(rotation,int) or isinstance(rotation,bool) or rotation <= 0:
            raise ValueError(f"item {index} has invalid secret metadata")
        if age > rotation:
            findings.append(Finding("rotation_overdue", "high", index, f"{name} is overdue for rotation."))
        if not owner:
            findings.append(Finding("missing_owner", "high", index, f"{name} has no owner."))
        if item.get("expires_in_days") is None:
            findings.append(Finding("no_expiry", "medium", index, f"{name} has no declared expiry."))
        if str(item.get("scope","")).lower() == "global":
            findings.append(Finding("global_scope", "high", index, f"{name} has global scope."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (
        ["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class SecretLeaseAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
