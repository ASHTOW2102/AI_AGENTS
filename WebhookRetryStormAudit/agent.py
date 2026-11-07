"""Flags webhook delivery configurations prone to retry storms against degraded receivers."""
from typing import Any


def audit(webhook: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if webhook.get("retry_backoff_strategy") == "fixed" and webhook.get("max_retries", 0) > 5:
        findings.append({"severity": "high", "issue": "Fixed backoff with many retries risks a retry storm on a degraded receiver."})
    if not webhook.get("circuit_breaker_enabled"):
        findings.append({"severity": "medium", "issue": "No circuit breaker to stop retries against a persistently failing endpoint."})
    return findings
