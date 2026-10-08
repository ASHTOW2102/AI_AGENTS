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
        raise ValueError("redirect chains must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        name = str(item.get("name", "")).strip()
        urls = item.get("urls")
        if not name or not isinstance(urls, list) or len(urls) < 2 or not all(isinstance(x, str) and x.startswith(("http://","https://")) for x in urls):
            raise ValueError(f"item {index} requires a name and at least two HTTP URLs")
        if len(set(urls)) != len(urls):
            findings.append(Finding("redirect_loop", "critical", index, f"{name} repeats a URL."))
        if any(a.startswith("https://") and b.startswith("http://") for a,b in zip(urls, urls[1:])):
            findings.append(Finding("https_downgrade", "critical", index, f"{name} downgrades from HTTPS to HTTP."))
        if len(urls) - 1 > 3:
            findings.append(Finding("too_many_hops", "medium", index, f"{name} has more than three redirects."))
    codes = sorted({finding.code for finding in findings})
    recommendations = (
        ["Review and resolve: " + ", ".join(codes) + ".", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class RedirectRadarAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
