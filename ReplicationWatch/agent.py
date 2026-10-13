from __future__ import annotations
import json
from dataclasses import asdict, dataclass
from typing import Any
RULES=json.loads(r'''[["lag_seconds","gt",60,"high_lag","high","Replica lag exceeds one minute."],["healthy","false",null,"unhealthy_replica","critical","Replica is unhealthy."],["failover_test_days","gt",90,"stale_failover_test","high","Failover has not been tested recently."],["cross_region","false",null,"single_region","medium","Replica is not cross-region."]]''')
@dataclass(frozen=True)
class Finding:
    code:str; severity:str; item:int; message:str
@dataclass(frozen=True)
class AuditReport:
    healthy:bool; items_checked:int; findings:list[Finding]; recommendations:list[str]
    def to_dict(self)->dict[str,Any]: return asdict(self)
def _bad(item,field,op,target):
    value=item.get(field)
    if op=="missing": return value is None or (isinstance(value,str) and not value.strip())
    if op=="true": return value is True
    if op=="false": return value is False
    if op=="eq": return value==target
    if op=="gt":
        if not isinstance(value,(int,float)) or isinstance(value,bool): raise ValueError(f"{field} must be numeric")
        return value>target
    if op=="gt_field":
        other=item.get(str(target))
        if not isinstance(value,(int,float)) or isinstance(value,bool) or not isinstance(other,(int,float)) or isinstance(other,bool): raise ValueError(f"{field} and {target} must be numeric")
        return value>other
    raise ValueError(f"unsupported operator {op}")
def audit(items:list[dict[str,Any]])->AuditReport:
    if not isinstance(items,list) or not items: raise ValueError("items must be a non-empty JSON array")
    findings=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict): raise ValueError(f"item {index} must be an object")
        for field,op,target,code,severity,message in RULES:
            if _bad(item,field,op,target): findings.append(Finding(code,severity,index,message))
    codes=sorted({x.code for x in findings})
    return AuditReport(not findings,len(items),findings,(["Review and resolve: "+", ".join(codes)+".","Confirm findings before live changes."] if findings else ["No configured risks were detected."]))
class ReplicationWatchAgent:
    def inspect(self,items:list[dict[str,Any]])->AuditReport: return audit(items)
