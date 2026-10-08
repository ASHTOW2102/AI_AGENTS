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
        raise ValueError("forms must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        name = str(item.get("name", "")).strip()
        method = str(item.get("method", "")).upper()
        action = str(item.get("action", ""))
        fields = item.get("fields")
        if not name or method not in {"GET","POST"} or not isinstance(fields, list):
            raise ValueError(f"item {index} has an invalid form definition")
        if not action.startswith("https://"):
            findings.append(Finding("insecure_action", "high", index, f"{name} does not submit over HTTPS."))
        sensitive = [f for f in fields if isinstance(f,dict) and str(f.get("type","")).lower() in {"password","hidden"}]
        if method == "GET" and sensitive:
            findings.append(Finding("sensitive_get", "critical", index, f"{name} sends sensitive fields in a URL."))
        if method == "POST" and item.get("csrf") is not True:
            findings.append(Finding("missing_csrf", "high", index, f"{name} lacks declared CSRF protection."))
        if any(str(f.get("type","")).lower()=="password" and str(f.get("autocomplete","")).lower() not in {"current-password","new-password","off"} for f in fields if isinstance(f,dict)):
            findings.append(Finding("unsafe_password_autocomplete", "medium", index, f"{name} has unsafe password autocomplete."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (
        ["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class FormGuardAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
