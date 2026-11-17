"""Flags web pages with no Referrer-Policy header, leaking full URLs including query parameters to third-party sites."""
from typing import Any


def audit(page: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not page.get("referrer_policy"):
        findings.append({"severity": "medium", "issue": "No Referrer-Policy header is set."})
    if page.get("referrer_policy") == "unsafe-url" and page.get("urls_contain_sensitive_query_params"):
        findings.append({"severity": "high", "issue": "unsafe-url referrer policy leaks sensitive query parameters to third parties."})
    return findings
