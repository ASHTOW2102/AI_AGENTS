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
        raise ValueError("dependencies must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        name=str(item.get("name","")).strip(); license_name=str(item.get("license","")).strip()
        if not name: raise ValueError(f"item {index}.name is required")
        if not license_name or license_name.upper() in {"UNKNOWN","NONE","N/A"}: findings.append(Finding("unknown_license","high",index,f"{name} has no known license."))
        if item.get("approved") is not True: findings.append(Finding("unapproved_license","high",index,f"{name} is not policy-approved."))
        if item.get("attribution_present") is not True: findings.append(Finding("missing_attribution","medium",index,f"{name} lacks recorded attribution."))
        if license_name.upper() in {"GPL-3.0","AGPL-3.0"}: findings.append(Finding("strong_copyleft","medium",index,f"{name} requires copyleft review."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class LicenseLensAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
