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
    if not isinstance(items,list) or not items:
        raise ValueError("password policies must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict):
            raise ValueError(f"item {index} must be an object")
        app=str(item.get("application","")).strip(); length=item.get("min_length")
        if not app or not isinstance(length,int) or isinstance(length,bool) or length <= 0: raise ValueError(f"item {index} has invalid policy metadata")
        if length < 12: findings.append(Finding("short_password","high",index,f"{app} permits passwords shorter than 12 characters."))
        if item.get("breach_check") is not True: findings.append(Finding("missing_breach_check","high",index,f"{app} does not check breached passwords."))
        if item.get("secure_reset") is not True: findings.append(Finding("unsafe_reset","critical",index,f"{app} lacks a secure reset flow."))
        if item.get("lockout_attempts") is None: findings.append(Finding("no_lockout","medium",index,f"{app} has no lockout threshold."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class PasswordGuardAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport:
        return audit(items)
