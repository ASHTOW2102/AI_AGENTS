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
        raise ValueError("robots policies must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        host=str(item.get("host","")).strip(); disallow=item.get("disallow"); allow=item.get("allow"); delay=item.get("crawl_delay",0)
        if not host or not isinstance(disallow,list) or not isinstance(allow,list) or not all(isinstance(x,str) for x in disallow+allow):
            raise ValueError(f"item {index} has invalid robots metadata")
        if "/" in disallow: findings.append(Finding("blanket_block","high",index,f"{host} blocks the entire site."))
        if any(any(word in path.lower() for word in ("private","admin","secret")) for path in allow):
            findings.append(Finding("sensitive_allow","critical",index,f"{host} explicitly allows a sensitive-looking path."))
        if not str(item.get("sitemap","")).startswith("https://"):
            findings.append(Finding("missing_sitemap","medium",index,f"{host} lacks an HTTPS sitemap."))
        if not isinstance(delay,(int,float)) or isinstance(delay,bool) or delay < 0: raise ValueError(f"item {index}.crawl_delay is invalid")
        if delay > 60: findings.append(Finding("high_crawl_delay","medium",index,f"{host} crawl delay exceeds 60 seconds."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings, len(items), findings, recommendations)

class RobotsGuardAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
