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
    if not isinstance(items,list) or not items: raise ValueError("datasets must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict): raise ValueError(f"item {index} must be an object")
        dataset=str(item.get("dataset","")).strip(); age=item.get("key_age_days"); algorithm=str(item.get("algorithm","")).upper()
        if not dataset or not isinstance(age,int) or isinstance(age,bool) or age<0: raise ValueError(f"item {index} has invalid encryption metadata")
        if item.get("encrypted") is not True: findings.append(Finding("not_encrypted","critical",index,f"{dataset} is not encrypted."))
        if algorithm in {"","DES","3DES","RC4","AES-ECB"}: findings.append(Finding("weak_algorithm","critical",index,f"{dataset} uses a weak or unknown algorithm."))
        if item.get("dedicated_key") is not True: findings.append(Finding("shared_key","high",index,f"{dataset} does not use a dedicated key."))
        if age>365: findings.append(Finding("stale_key","high",index,f"{dataset} key is older than one year."))
    codes=sorted({x.code for x in findings})
    return AuditReport(not findings,len(items),findings,(["Review and resolve: "+", ".join(codes)+".","Confirm findings before live changes."] if findings else ["No configured risks were detected."]))

class EncryptionAuditAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport: return audit(items)
