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
        raise ValueError("responses must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        url = str(item.get("url", "")).strip()
        headers = item.get("headers")
        if not url or not isinstance(headers, dict):
            raise ValueError(f"item {index} requires url and headers")
        normalized = {str(k).lower(): str(v) for k, v in headers.items()}
        required = {"strict-transport-security":"missing_hsts","content-security-policy":"missing_csp","x-content-type-options":"missing_nosniff","referrer-policy":"missing_referrer_policy"}
        for header, code in required.items():
            if header not in normalized:
                findings.append(Finding(code, "high", index, f"{url} is missing {header}."))
        if normalized.get("access-control-allow-origin") == "*":
            findings.append(Finding("wildcard_cors", "medium", index, f"{url} allows every cross-origin origin."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (
        ["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class HeaderHawkAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
