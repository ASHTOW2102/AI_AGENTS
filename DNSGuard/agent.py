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
        raise ValueError("domains must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        domain = str(item.get("domain", "")).strip()
        if not domain or "." not in domain:
            raise ValueError(f"item {index}.domain is invalid")
        for field, code, severity in (("spf","missing_spf","high"),("dmarc","missing_dmarc","high"),("caa","missing_caa","medium")):
            if item.get(field) is not True:
                findings.append(Finding(code, severity, index, f"{domain} is missing {field.upper()}."))
        if item.get("wildcard") is True:
            findings.append(Finding("wildcard_record", "medium", index, f"{domain} uses a wildcard DNS record."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings before changing live systems."] if findings else ["No configured risks were detected."])
    return AuditReport(not findings, len(items), findings, recommendations)

class DNSGuardAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
