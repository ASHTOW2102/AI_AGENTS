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
        raise ValueError("health checks must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict):
            raise ValueError(f"item {index} must be an object")
        service=str(item.get("service","")).strip(); interval=item.get("interval_seconds"); timeout=item.get("timeout_seconds")
        if not service or not isinstance(interval,int) or isinstance(interval,bool) or interval <= 0 or not isinstance(timeout,int) or isinstance(timeout,bool) or timeout <= 0: raise ValueError(f"item {index} has invalid health-check metadata")
        if interval > 60: findings.append(Finding("long_interval","medium",index,f"{service} is checked less than once per minute."))
        if timeout > 10: findings.append(Finding("slow_timeout","medium",index,f"{service} timeout exceeds 10 seconds."))
        if item.get("checks_dependencies") is not True: findings.append(Finding("dependencies_ignored","high",index,f"{service} ignores dependencies."))
        if str(item.get("check_type","")).lower() in {"tcp","process","ping"}: findings.append(Finding("shallow_check","high",index,f"{service} uses a shallow health check."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class HealthProbeAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport:
        return audit(items)
