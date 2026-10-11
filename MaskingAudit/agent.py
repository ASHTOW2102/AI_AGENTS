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
        raise ValueError("data fields must be a non-empty JSON array")
    findings: list[Finding]=[]
    for index,item in enumerate(items,1):
        if not isinstance(item,dict):
            raise ValueError(f"item {index} must be an object")
        field=str(item.get("field","")).strip(); classification=str(item.get("classification","")).lower()
        if not field or classification not in {"public","internal","personal","payment","health","secret"}: raise ValueError(f"item {index} has invalid field metadata")
        sensitive=classification in {"personal","payment","health","secret"}
        if sensitive and item.get("masked") is not True: findings.append(Finding("unmasked_sensitive","critical",index,f"{field} is sensitive and unmasked."))
        if sensitive and item.get("reversible") is True: findings.append(Finding("reversible_masking","high",index,f"{field} uses reversible masking."))
        if sensitive and item.get("sample_present") is True: findings.append(Finding("sample_exposed","critical",index,f"{field} includes a real sample."))
        if not str(item.get("owner","")).strip(): findings.append(Finding("missing_owner","medium",index,f"{field} has no owner."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class MaskingAuditAgent:
    def inspect(self,items: list[dict[str,Any]]) -> AuditReport:
        return audit(items)
