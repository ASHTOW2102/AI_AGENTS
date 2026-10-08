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
        raise ValueError("retention policies must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        dataset = str(item.get("dataset", "")).strip()
        if not dataset:
            raise ValueError(f"item {index}.dataset is required")
        days = item.get("retention_days")
        if days is None:
            findings.append(Finding("indefinite_retention", "critical", index, f"{dataset} has indefinite retention."))
        elif not isinstance(days,int) or isinstance(days,bool) or days <= 0:
            raise ValueError(f"item {index}.retention_days must be positive or null")
        elif days > 2555:
            findings.append(Finding("excessive_retention", "high", index, f"{dataset} is retained for over seven years."))
        if not str(item.get("legal_basis","")).strip():
            findings.append(Finding("missing_legal_basis", "high", index, f"{dataset} has no stated legal basis."))
        if not str(item.get("deletion_method","")).strip():
            findings.append(Finding("missing_deletion_method", "high", index, f"{dataset} has no deletion method."))
        if not str(item.get("owner","")).strip():
            findings.append(Finding("missing_owner", "medium", index, f"{dataset} has no owner."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (
        ["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class RetentionCheckAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
