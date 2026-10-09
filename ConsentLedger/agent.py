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
        raise ValueError("consent records must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        subject = str(item.get("subject_id", "")).strip(); purpose=str(item.get("purpose","")).strip().lower()
        age=item.get("age_days"); valid=item.get("valid_days")
        if not subject or not isinstance(age,int) or isinstance(age,bool) or age < 0 or not isinstance(valid,int) or isinstance(valid,bool) or valid <= 0:
            raise ValueError(f"item {index} has invalid consent metadata")
        if item.get("evidence") is not True:
            findings.append(Finding("missing_evidence","high",index,f"{subject} has no consent evidence."))
        if purpose in {"","all","general"}:
            findings.append(Finding("vague_purpose","high",index,f"{subject} has a vague purpose."))
        if age > valid:
            findings.append(Finding("expired_consent","critical",index,f"{subject} consent has expired."))
        if item.get("withdrawal_available") is not True:
            findings.append(Finding("no_withdrawal","high",index,f"{subject} has no withdrawal path."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings, len(items), findings, recommendations)

class ConsentLedgerAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
