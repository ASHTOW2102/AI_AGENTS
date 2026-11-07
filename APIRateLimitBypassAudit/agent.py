"""Detects API endpoints where rate limiting can be bypassed via alternate identifiers."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("rate_limit_key") == "ip" and endpoint.get("supports_proxy_rotation"):
        findings.append({"severity": "high", "issue": "IP-based rate limiting can be bypassed via proxy rotation."})
    if not endpoint.get("authenticated_rate_limit_key"):
        findings.append({"severity": "medium", "issue": "No authenticated identity is used as a rate limit key."})
    return findings
