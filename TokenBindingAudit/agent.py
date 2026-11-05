"""Checks bearer-token usage for device/client binding to limit replay if a token is stolen."""
from typing import Any


def audit(token: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if token.get("highly_privileged") and not token.get("bound_to_client_or_device"):
        findings.append({"severity": "high", "issue": "Highly privileged token is a bare bearer token with no client binding."})
    if token.get("bound_to_client_or_device") and not token.get("binding_verified_on_each_use"):
        findings.append({"severity": "medium", "issue": "Token binding is established but not verified on every use."})
    if token.get("transmitted_via_url_query_param"):
        findings.append({"severity": "high", "issue": "Token is transmitted via URL query parameter, risking log exposure."})
    return findings
