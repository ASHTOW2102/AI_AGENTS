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
        raise ValueError("invoices must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        number = str(item.get("number", "")).strip()
        if not number:
            raise ValueError(f"item {index}.number is required")
        values = {}
        for field in ("subtotal","tax","total","paid"):
            value=item.get(field)
            if not isinstance(value,(int,float)) or isinstance(value,bool):
                raise ValueError(f"item {index}.{field} must be numeric")
            values[field]=float(value)
        if values["subtotal"] < 0 or values["tax"] < 0 or values["total"] < 0:
            findings.append(Finding("negative_amount", "high", index, f"{number} contains a negative charge."))
        if round(values["subtotal"]+values["tax"],2) != round(values["total"],2):
            findings.append(Finding("total_mismatch", "critical", index, f"{number} total does not equal subtotal plus tax."))
        if values["paid"] < 0:
            findings.append(Finding("negative_payment", "high", index, f"{number} has a negative payment."))
        if values["paid"] < values["total"]:
            findings.append(Finding("outstanding_balance", "medium", index, f"{number} is not fully paid."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings, len(items), findings, recommendations)

class InvoiceAuditAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
