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
        raise ValueError("scripts must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict):
            raise ValueError(f"item {index} must be an object")
        src=str(item.get("src","")).strip(); pages=item.get("pages")
        if not src or not isinstance(pages,int) or isinstance(pages,bool) or pages < 0: raise ValueError(f"item {index} has invalid script metadata")
        if not src.startswith("https://"): findings.append(Finding("insecure_origin","critical",index,f"{src} is not HTTPS."))
        if item.get("integrity") is not True: findings.append(Finding("missing_integrity","high",index,f"{src} lacks an integrity hash."))
        if not str(item.get("owner","")).strip(): findings.append(Finding("missing_owner","high",index,f"{src} has no owner."))
        if item.get("approved") is not True: findings.append(Finding("unapproved_script","high",index,f"{src} is not approved."))
        if pages > 100: findings.append(Finding("broad_coverage","medium",index,f"{src} runs on over 100 pages."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class ScriptSentryAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport:
        return audit(items)
