"""Flags services in a mesh where a global rate limit decision made at the edge is not propagated to internal callers, letting internal retries bypass it."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if service.get("edge_rate_limited") and not service.get("rate_limit_decision_propagated_internally"):
        findings.append({"severity": "medium", "issue": "Edge rate-limit decisions are not propagated to internal service-to-service calls."})
    if service.get("internal_retries_enabled") and not service.get("rate_limit_decision_propagated_internally"):
        findings.append({"severity": "high", "issue": "Internal retries can bypass the edge rate limit entirely since the decision isn't propagated."})
    return findings
