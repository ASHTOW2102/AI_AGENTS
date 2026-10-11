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
        raise ValueError("firewall rules must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict):
            raise ValueError(f"item {index} must be an object")
        name=str(item.get("name","")).strip(); source=str(item.get("source","")).strip(); port=item.get("port")
        if not name or not source or not isinstance(port,int) or isinstance(port,bool) or not 1 <= port <= 65535: raise ValueError(f"item {index} has invalid firewall metadata")
        world=source in {"0.0.0.0/0","::/0"}
        if world and port in {22,23,3389,5432,3306}: findings.append(Finding("open_admin_port","critical",index,f"{name} exposes an administrative port globally."))
        elif world and port not in {80,443}: findings.append(Finding("world_open","high",index,f"{name} is globally accessible."))
        if not str(item.get("owner","")).strip(): findings.append(Finding("missing_owner","high",index,f"{name} has no owner."))
        if item.get("temporary") is True and item.get("expires_in_days") is None: findings.append(Finding("temporary_no_expiry","high",index,f"{name} is temporary without expiry."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class FirewallLensAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport:
        return audit(items)
