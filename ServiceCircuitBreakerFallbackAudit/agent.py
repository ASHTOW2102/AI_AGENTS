"""Checks circuit-breaker fallback behavior for safe degradation when breakers trip."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if service.get("circuit_breaker_enabled") and not service.get("fallback_defined"):
        findings.append({"severity": "high", "issue": "Circuit breaker has no fallback behavior defined."})
    if service.get("fallback_defined") and service.get("fallback_returns_cached_data") and not service.get("staleness_indicated_to_caller"):
        findings.append({"severity": "medium", "issue": "Cached fallback data does not indicate staleness to the caller."})
    if service.get("fallback_silently_succeeds_on_critical_write"):
        findings.append({"severity": "critical", "issue": "Fallback silently reports success for a critical write that did not occur."})
    return findings
