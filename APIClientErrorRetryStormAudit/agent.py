"""Checks client retry logic for storm risk when a dependency returns sustained errors."""
from typing import Any


def audit(client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if client.get("retries_on_4xx"):
        findings.append({"severity": "high", "issue": "Client retries on 4xx client errors, which will not succeed on retry."})
    if client.get("retry_enabled") and not client.get("jitter_applied"):
        findings.append({"severity": "medium", "issue": "Retry logic has no jitter, risking synchronized retry storms."})
    if client.get("retry_enabled") and not client.get("circuit_breaker_coordinated"):
        findings.append({"severity": "medium", "issue": "Retries are not coordinated with a circuit breaker to stop during outages."})
    return findings
