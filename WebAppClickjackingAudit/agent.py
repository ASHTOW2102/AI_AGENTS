"""Flags web pages missing frame-busting headers that would allow clickjacking via iframe embedding."""
from typing import Any


def audit(page: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not page.get("x_frame_options") and "frame-ancestors" not in page.get("csp_directives", []):
        findings.append({"severity": "high", "issue": "Page has no X-Frame-Options or CSP frame-ancestors directive."})
    if page.get("x_frame_options") == "ALLOWALL":
        findings.append({"severity": "high", "issue": "X-Frame-Options is explicitly set to allow all framing."})
    return findings
