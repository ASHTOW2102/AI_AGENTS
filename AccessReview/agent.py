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
        raise ValueError("access records must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        user = str(item.get("user", "")).strip(); role = str(item.get("role","")).lower()
        inactive = item.get("inactive_days"); reviewed = item.get("reviewed_days_ago")
        if not user or not isinstance(inactive,int) or isinstance(inactive,bool) or inactive < 0:
            raise ValueError(f"item {index} has invalid account metadata")
        if inactive > 90:
            findings.append(Finding("dormant_account", "high", index, f"{user} is dormant."))
        if role in {"admin","owner","superuser"}:
            findings.append(Finding("privileged_account", "medium", index, f"{user} has a privileged role requiring review."))
        if not str(item.get("owner","")).strip():
            findings.append(Finding("missing_owner", "high", index, f"{user} has no accountable owner."))
        if reviewed is None:
            findings.append(Finding("never_reviewed", "high", index, f"{user} has no review date."))
        elif not isinstance(reviewed,int) or isinstance(reviewed,bool) or reviewed < 0:
            raise ValueError(f"item {index}.reviewed_days_ago must be non-negative or null")
        elif reviewed > 90:
            findings.append(Finding("stale_review", "medium", index, f"{user} was reviewed over 90 days ago."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (
        ["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class AccessReviewAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
