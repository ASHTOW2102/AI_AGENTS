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
        raise ValueError("tokens must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        name=str(item.get("name","")).strip(); scopes=item.get("scopes"); last=item.get("last_used_days_ago")
        if not name or not isinstance(scopes,list) or not all(isinstance(x,str) for x in scopes) or not isinstance(last,int) or isinstance(last,bool) or last < 0:
            raise ValueError(f"item {index} has invalid token metadata")
        if any(scope.lower() in {"admin","root","write:*","*"} for scope in scopes): findings.append(Finding("privileged_scope","critical",index,f"{name} has a privileged scope."))
        if item.get("expires_in_days") is None: findings.append(Finding("no_expiry","high",index,f"{name} has no expiry."))
        if last > 90: findings.append(Finding("stale_token","high",index,f"{name} has not been used for over 90 days."))
        if not str(item.get("owner","")).strip(): findings.append(Finding("missing_owner","high",index,f"{name} has no owner."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings, len(items), findings, recommendations)

class TokenScopeAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
