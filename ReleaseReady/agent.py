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
        raise ValueError("releases must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        version = str(item.get("version", "")).strip()
        percent = item.get("initial_rollout_percent")
        if not version or not isinstance(percent,(int,float)) or isinstance(percent,bool) or not 0 < percent <= 100:
            raise ValueError(f"item {index} has invalid release metadata")
        if item.get("tests_passed") is not True:
            findings.append(Finding("tests_failed", "critical", index, f"{version} has no passing-test confirmation."))
        if item.get("rollback_plan") is not True:
            findings.append(Finding("missing_rollback", "high", index, f"{version} has no rollback plan."))
        if item.get("monitoring") is not True:
            findings.append(Finding("missing_monitoring", "high", index, f"{version} has no monitoring confirmation."))
        if not str(item.get("owner","")).strip():
            findings.append(Finding("missing_owner", "high", index, f"{version} has no release owner."))
        if percent == 100:
            findings.append(Finding("full_rollout", "medium", index, f"{version} starts at a full rollout."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (
        ["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class ReleaseReadyAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
