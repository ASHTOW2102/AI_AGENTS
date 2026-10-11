from __future__ import annotations
import json
from dataclasses import asdict, dataclass
from typing import Any

RULES = json.loads(r'''[["unsubscribe","false",null,"missing_unsubscribe","high","Template lacks an unsubscribe path."],["plaintext","false",null,"missing_plaintext","medium","Template lacks a plaintext version."],["subject","missing",null,"missing_subject","high","Template has no subject."],["owner","missing",null,"missing_owner","medium","Template has no owner."]]''')

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

def _violates(item: dict[str, Any], field: str, op: str, target: Any) -> bool:
    value=item.get(field)
    if op=="missing": return value is None or (isinstance(value,str) and not value.strip())
    if op=="true": return value is True
    if op=="false": return value is False
    if op=="not_prefix": return not isinstance(value,str) or not value.startswith(str(target))
    if op=="gt":
        if not isinstance(value,(int,float)) or isinstance(value,bool): raise ValueError(f"{field} must be numeric")
        return value > target
    if op=="gt_field":
        other=item.get(str(target))
        if not isinstance(value,(int,float)) or isinstance(value,bool) or not isinstance(other,(int,float)) or isinstance(other,bool): raise ValueError(f"{field} and {target} must be numeric")
        return value > other
    raise ValueError(f"unsupported rule operator: {op}")

def audit(items: list[dict[str, Any]]) -> AuditReport:
    if not isinstance(items,list) or not items: raise ValueError("items must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict): raise ValueError(f"item {index} must be an object")
        for field,op,target,code,severity,message in RULES:
            if _violates(item,field,op,target): findings.append(Finding(code,severity,index,message))
    codes=sorted({x.code for x in findings})
    recs=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before live changes."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recs)

class EmailTemplateAuditAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport: return audit(items)
