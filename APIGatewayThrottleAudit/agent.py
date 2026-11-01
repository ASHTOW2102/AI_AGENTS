"""Checks API gateway throttling configuration for per-client fairness and burst handling."""
from typing import Any


def audit(route: dict[str, Any]):
    findings = []
    if not route.get("throttle_configured"):
        findings.append({"severity": "high", "issue": "Route has no throttling configured."})
    if route.get("throttle_configured") and not route.get("per_client_key"):
        findings.append({"severity": "medium", "issue": "Throttling is not scoped per client."})
    if route.get("burst_limit", 0) < route.get("steady_rate_limit", 0):
        findings.append({"severity": "low", "issue": "Burst limit is lower than the steady rate limit."})
    return findings
