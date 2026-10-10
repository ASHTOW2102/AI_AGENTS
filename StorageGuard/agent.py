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
        raise ValueError("buckets must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        name=str(item.get("name","")).strip()
        if not name: raise ValueError(f"item {index}.name is required")
        if item.get("public") is True: findings.append(Finding("public_bucket","critical",index,f"{name} is public."))
        if item.get("encryption") is not True: findings.append(Finding("missing_encryption","critical",index,f"{name} lacks encryption."))
        if item.get("versioning") is not True: findings.append(Finding("versioning_off","medium",index,f"{name} has versioning disabled."))
        retention=item.get("retention_days")
        if retention is None: findings.append(Finding("no_retention","high",index,f"{name} has no retention control."))
        elif not isinstance(retention,int) or isinstance(retention,bool) or retention <= 0: raise ValueError(f"item {index}.retention_days is invalid")
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class StorageGuardAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
