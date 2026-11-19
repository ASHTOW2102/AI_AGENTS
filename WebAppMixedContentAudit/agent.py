"""Flags HTTPS web pages that load active content (scripts, stylesheets) over plain HTTP, enabling man-in-the-middle injection."""
from typing import Any


def audit(page: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if page.get("served_over_https") and page.get("http_active_content_urls"):
        findings.append({"severity": "high", "issue": f"Page served over HTTPS loads active content over HTTP: {page.get('http_active_content_urls')}"})
    if not page.get("upgrade_insecure_requests_enabled"):
        findings.append({"severity": "low", "issue": "Page does not set upgrade-insecure-requests to auto-correct mixed content."})
    return findings
