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
        raise ValueError("images must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        path=str(item.get("path","")).strip(); size=item.get("bytes")
        if not path or not isinstance(size,int) or isinstance(size,bool) or size < 0: raise ValueError(f"item {index} has invalid image metadata")
        if size > 1000000: findings.append(Finding("oversized_image","high",index,f"{path} exceeds 1 MB."))
        if item.get("width") is None or item.get("height") is None: findings.append(Finding("missing_dimensions","medium",index,f"{path} lacks explicit dimensions."))
        if not str(item.get("alt","")).strip(): findings.append(Finding("missing_alt","high",index,f"{path} lacks alternative text."))
        if str(item.get("format","")).lower() not in {"webp","avif","svg","jpeg","jpg","png"}: findings.append(Finding("inefficient_format","medium",index,f"{path} uses an unsupported format."))
    codes=sorted({finding.code for finding in findings})
    recommendations=(["Review and resolve: "+", ".join(codes)+".","Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings,len(items),findings,recommendations)

class ImageBudgetAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
