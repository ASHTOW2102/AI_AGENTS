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
        raise ValueError("sitemap entries must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict):
            raise ValueError(f"item {index} must be an object")
        url=str(item.get("url","")).strip(); age=item.get("last_modified_days"); priority=item.get("priority")
        if not url or not isinstance(age,int) or isinstance(age,bool) or age < 0 or not isinstance(priority,(int,float)) or isinstance(priority,bool): raise ValueError(f"item {index} has invalid sitemap metadata")
        if not url.startswith("https://"): findings.append(Finding("insecure_url","high",index,f"{url} is not HTTPS."))
        if age > 365: findings.append(Finding("stale_page","medium",index,f"{url} has not changed for over one year."))
        if not 0 <= priority <= 1: findings.append(Finding("invalid_priority","medium",index,f"{url} has priority outside 0 to 1."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class SitemapScoutAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport:
        return audit(items)
