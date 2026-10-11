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
        raise ValueError("services must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict):
            raise ValueError(f"item {index} must be an object")
        name=str(item.get("name","")).strip(); tier=item.get("tier"); age=item.get("docs_age_days")
        if not name or not isinstance(tier,int) or isinstance(tier,bool) or not isinstance(age,int) or isinstance(age,bool) or age < 0: raise ValueError(f"item {index} has invalid service metadata")
        if not str(item.get("owner","")).strip(): findings.append(Finding("missing_owner","high",index,f"{name} has no owner."))
        if not str(item.get("repository","")).strip(): findings.append(Finding("missing_repository","medium",index,f"{name} has no repository."))
        if tier not in {1,2,3,4}: findings.append(Finding("invalid_tier","medium",index,f"{name} has an invalid tier."))
        if age > 180: findings.append(Finding("stale_docs","medium",index,f"{name} documentation is stale."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class ServiceCatalogAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport:
        return audit(items)
