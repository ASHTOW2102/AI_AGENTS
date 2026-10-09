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
        raise ValueError("session policies must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        app=str(item.get("application","")).strip(); idle=item.get("idle_minutes"); absolute=item.get("absolute_minutes")
        if not app or not isinstance(idle,int) or isinstance(idle,bool) or idle <= 0 or not isinstance(absolute,int) or isinstance(absolute,bool) or absolute <= 0:
            raise ValueError(f"item {index} has invalid session metadata")
        if idle > 60: findings.append(Finding("long_idle","high",index,f"{app} idle timeout exceeds one hour."))
        if absolute > 1440: findings.append(Finding("long_absolute","medium",index,f"{app} session exceeds one day."))
        if item.get("rotate_on_login") is not True: findings.append(Finding("no_rotation","high",index,f"{app} does not rotate sessions on login."))
        if item.get("secure_cookie") is not True: findings.append(Finding("insecure_cookie","critical",index,f"{app} lacks secure session cookies."))
        if item.get("max_sessions") is None: findings.append(Finding("unlimited_sessions","medium",index,f"{app} allows unlimited concurrent sessions."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings, len(items), findings, recommendations)

class SessionSentryAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
