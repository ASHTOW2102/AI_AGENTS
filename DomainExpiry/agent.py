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
        raise ValueError("domains must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        domain=str(item.get("domain","")).strip(); days=item.get("days_remaining")
        if not domain or "." not in domain or not isinstance(days,int) or isinstance(days,bool): raise ValueError(f"item {index} has invalid domain metadata")
        if days < 0: findings.append(Finding("expired","critical",index,f"{domain} has expired."))
        elif days <= 30: findings.append(Finding("expires_soon","high",index,f"{domain} expires within 30 days."))
        if item.get("auto_renew") is not True: findings.append(Finding("auto_renew_off","high",index,f"{domain} has auto-renewal disabled."))
        if not str(item.get("owner","")).strip(): findings.append(Finding("missing_owner","high",index,f"{domain} has no owner."))
        if item.get("registrar_lock") is not True: findings.append(Finding("registrar_unlocked","high",index,f"{domain} lacks registrar lock."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class DomainExpiryAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
