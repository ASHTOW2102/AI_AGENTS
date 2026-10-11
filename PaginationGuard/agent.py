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
    if not isinstance(items,list) or not items: raise ValueError("endpoints must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict): raise ValueError(f"item {index} must be an object")
        endpoint=str(item.get("endpoint","")).strip(); default=item.get("default_limit"); maximum=item.get("max_limit")
        if not endpoint or not isinstance(maximum,int) or isinstance(maximum,bool) or maximum<=0: raise ValueError(f"item {index} has invalid pagination metadata")
        if default is None: findings.append(Finding("no_default_limit","high",index,f"{endpoint} has no default limit."))
        elif not isinstance(default,int) or isinstance(default,bool) or default<=0: raise ValueError(f"item {index}.default_limit is invalid")
        if maximum>1000: findings.append(Finding("excessive_max_limit","high",index,f"{endpoint} permits over 1000 results."))
        if item.get("stable_sort") is not True: findings.append(Finding("unstable_sort","medium",index,f"{endpoint} lacks stable ordering."))
        if item.get("continuation_token") is not True: findings.append(Finding("missing_token","medium",index,f"{endpoint} lacks continuation tokens."))
    codes=sorted({x.code for x in findings})
    return AuditReport(not findings,len(items),findings,(["Review and resolve: "+", ".join(codes)+".","Confirm findings before live changes."] if findings else ["No configured risks were detected."]))

class PaginationGuardAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport: return audit(items)
