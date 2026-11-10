"""Audits service mesh circuit breaker thresholds for defaults that are too permissive to protect downstream services."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not service.get("circuit_breaker_configured"):
        findings.append({"severity": "high", "issue": "No circuit breaker is configured for this service."})
    if service.get("consecutive_errors_threshold", 0) > service.get("recommended_max_threshold", 5):
        findings.append({"severity": "medium", "issue": "Circuit breaker error threshold is looser than recommended."})
    return findings
