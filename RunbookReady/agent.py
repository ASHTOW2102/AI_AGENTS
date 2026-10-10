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
        raise ValueError("runbooks must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        service=str(item.get("service","")).strip(); reviewed=item.get("reviewed_days_ago"); tested=item.get("tested_days_ago")
        if not service or not isinstance(reviewed,int) or isinstance(reviewed,bool) or reviewed < 0: raise ValueError(f"item {index} has invalid runbook metadata")
        if not str(item.get("owner","")).strip(): findings.append(Finding("missing_owner","high",index,f"{service} has no runbook owner."))
        if reviewed > 180: findings.append(Finding("stale_runbook","high",index,f"{service} runbook is stale."))
        if item.get("rollback_steps") is not True: findings.append(Finding("missing_rollback","critical",index,f"{service} lacks rollback steps."))
        if tested is None: findings.append(Finding("never_tested","high",index,f"{service} runbook has never been tested."))
        elif not isinstance(tested,int) or isinstance(tested,bool) or tested < 0: raise ValueError(f"item {index}.tested_days_ago is invalid")
        if item.get("contacts") is not True: findings.append(Finding("missing_contacts","medium",index,f"{service} lacks escalation contacts."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class RunbookReadyAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
