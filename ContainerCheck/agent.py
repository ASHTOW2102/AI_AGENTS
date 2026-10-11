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
        raise ValueError("containers must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict):
            raise ValueError(f"item {index} must be an object")
        name=str(item.get("name","")).strip()
        if not name: raise ValueError(f"item {index}.name is required")
        if item.get("run_as_root") is True: findings.append(Finding("runs_as_root","critical",index,f"{name} runs as root."))
        if item.get("privileged") is True: findings.append(Finding("privileged","critical",index,f"{name} is privileged."))
        if item.get("read_only_root") is not True: findings.append(Finding("writable_root","high",index,f"{name} has a writable root filesystem."))
        if item.get("cpu_limit") is not True: findings.append(Finding("missing_cpu_limit","medium",index,f"{name} has no CPU limit."))
        if item.get("memory_limit") is not True: findings.append(Finding("missing_memory_limit","medium",index,f"{name} has no memory limit."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class ContainerCheckAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport:
        return audit(items)
