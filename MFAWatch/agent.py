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
        raise ValueError("accounts must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        user=str(item.get("user","")).strip(); factors=item.get("factors"); inactive=item.get("inactive_days")
        if not user or not isinstance(factors,list) or not all(isinstance(x,str) for x in factors) or not isinstance(inactive,int) or isinstance(inactive,bool) or inactive < 0: raise ValueError(f"item {index} has invalid account metadata")
        if item.get("mfa") is not True: findings.append(Finding("mfa_missing","critical",index,f"{user} does not have MFA."))
        if any(x.lower()=="sms" for x in factors): findings.append(Finding("weak_factor","medium",index,f"{user} relies on SMS."))
        if str(item.get("role","")).lower() in {"admin","owner"} and inactive > 90: findings.append(Finding("dormant_admin","critical",index,f"{user} is a dormant privileged account."))
        if item.get("recovery") is not True: findings.append(Finding("missing_recovery","high",index,f"{user} lacks a recovery method."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class MFAWatchAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
