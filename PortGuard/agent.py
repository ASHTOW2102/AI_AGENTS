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
    def to_dict(self) -> dict[str, Any]: return asdict(self)

def audit(items: list[dict[str, Any]]) -> AuditReport:
    if not isinstance(items,list) or not items: raise ValueError("services must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict): raise ValueError(f"item {index} must be an object")
        host=str(item.get("host","")).strip(); port=item.get("port"); protocol=str(item.get("protocol","")).lower()
        if not host or not isinstance(port,int) or isinstance(port,bool) or not 1<=port<=65535: raise ValueError(f"item {index} has invalid service metadata")
        if item.get("public") is True and port in {22,23,3306,5432,6379,3389}: findings.append(Finding("public_admin_port","critical",index,f"{host}:{port} is publicly exposed."))
        if protocol in {"http","ftp","telnet","postgres","mysql","redis"}: findings.append(Finding("unencrypted_protocol","high",index,f"{host}:{port} uses an unencrypted protocol."))
        if not str(item.get("owner","")).strip(): findings.append(Finding("missing_owner","high",index,f"{host}:{port} has no owner."))
        if item.get("debug") is True: findings.append(Finding("debug_service","high",index,f"{host}:{port} is marked as debug."))
    codes=sorted({x.code for x in findings})
    return AuditReport(not findings,len(items),findings,(["Review and resolve: "+", ".join(codes)+".","Confirm findings before live changes."] if findings else ["No configured risks were detected."]))

class PortGuardAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport: return audit(items)
