"""Flags pages with no Content-Security-Policy header, or one that allows 'unsafe-inline' script execution."""
from typing import Any


def audit(page: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not page.get("csp_header_present"):
        findings.append({"severity": "high", "issue": "Page has no Content-Security-Policy header."})
    elif page.get("csp_allows_unsafe_inline"):
        findings.append({"severity": "medium", "issue": "CSP header allows 'unsafe-inline' script execution."})
    return findings
