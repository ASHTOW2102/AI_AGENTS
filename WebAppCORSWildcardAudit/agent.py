"""Flags web API endpoints that respond with Access-Control-Allow-Origin: * while also allowing credentialed requests."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("cors_allow_origin") == "*" and endpoint.get("cors_allow_credentials"):
        findings.append({"severity": "high", "issue": "Wildcard CORS origin combined with allow-credentials exposes authenticated responses to any site."})
    if endpoint.get("cors_allow_origin") == "*" and endpoint.get("serves_sensitive_data"):
        findings.append({"severity": "medium", "issue": "Wildcard CORS origin is used on an endpoint serving sensitive data."})
    return findings
