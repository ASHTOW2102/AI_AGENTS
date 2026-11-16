"""Flags API gateway routes where internal service paths bypass the gateway's authentication layer."""
from typing import Any


def audit(route: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if route.get("reachable_directly") and route.get("requires_auth_at_gateway") and not route.get("requires_auth_at_service"):
        findings.append({"severity": "high", "issue": "Service is directly reachable and enforces no auth of its own if the gateway is bypassed."})
    if not route.get("gateway_enforces_auth"):
        findings.append({"severity": "high", "issue": "Gateway does not enforce authentication on this route."})
    return findings
