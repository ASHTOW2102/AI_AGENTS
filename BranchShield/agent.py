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
        raise ValueError("branches must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        repo=str(item.get("repository","")).strip(); branch=str(item.get("branch","")).strip(); reviews=item.get("required_reviews")
        if not repo or not branch or not isinstance(reviews,int) or isinstance(reviews,bool) or reviews < 0: raise ValueError(f"item {index} has invalid branch metadata")
        if reviews < 1: findings.append(Finding("no_reviews","high",index,f"{repo}/{branch} requires no review."))
        if item.get("status_checks") is not True: findings.append(Finding("missing_checks","high",index,f"{repo}/{branch} lacks required checks."))
        if item.get("force_push") is True: findings.append(Finding("force_push_allowed","critical",index,f"{repo}/{branch} allows force pushes."))
        if item.get("admin_bypass") is True: findings.append(Finding("admin_bypass","medium",index,f"{repo}/{branch} allows administrator bypass."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class BranchShieldAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
