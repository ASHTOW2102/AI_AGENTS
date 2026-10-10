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
        raise ValueError("alerts must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        name=str(item.get("name","")).strip(); frequency=item.get("fires_per_day"); message=str(item.get("message","")).strip().lower()
        if not name or not isinstance(frequency,(int,float)) or isinstance(frequency,bool) or frequency < 0: raise ValueError(f"item {index} has invalid alert metadata")
        if not str(item.get("owner","")).strip(): findings.append(Finding("missing_owner","high",index,f"{name} has no owner."))
        if frequency > 20: findings.append(Finding("noisy_alert","high",index,f"{name} fires more than 20 times daily."))
        if item.get("runbook") is not True: findings.append(Finding("missing_runbook","medium",index,f"{name} has no runbook."))
        if len(message) < 20 or message in {"error","something happened","failed"}: findings.append(Finding("vague_message","medium",index,f"{name} has a non-actionable message."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class AlertNoiseAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
