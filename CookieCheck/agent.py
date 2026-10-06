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
        raise ValueError("cookies must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        name = str(item.get("name", "")).strip()
        if not name:
            raise ValueError(f"item {index}.name is required")
        if not item.get("secure", False):
            findings.append(Finding("missing_secure", "high", index, f"{name} is not Secure."))
        if not item.get("http_only", False):
            findings.append(Finding("missing_http_only", "medium", index, f"{name} is readable by scripts."))
        same_site = str(item.get("same_site", "")).lower()
        if same_site not in {"strict", "lax"}:
            findings.append(Finding("weak_same_site", "high", index, f"{name} has weak or missing SameSite."))
        age = item.get("max_age_seconds", 0)
        if not isinstance(age, int) or isinstance(age, bool) or age < 0:
            raise ValueError(f"item {index}.max_age_seconds must be a non-negative integer")
        if age > 2592000:
            findings.append(Finding("long_lifetime", "medium", index, f"{name} lasts longer than 30 days."))
        if str(item.get("domain", "")).startswith("."):
            findings.append(Finding("broad_domain", "medium", index, f"{name} is shared across subdomains."))
    codes = {finding.code for finding in findings}
    recommendations = (
        [f"Review and resolve: {', '.join(sorted(codes))}.", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class CookieCheckAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
