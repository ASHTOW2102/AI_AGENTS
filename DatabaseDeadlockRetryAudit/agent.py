"""Checks database transaction deadlock handling for bounded retries and backoff."""
from typing import Any


def audit(transaction: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if transaction.get("deadlock_retry_enabled") and not transaction.get("max_retry_count"):
        findings.append({"severity": "medium", "issue": "Deadlock retry has no maximum retry count."})
    if transaction.get("deadlock_retry_enabled") and not transaction.get("backoff_strategy"):
        findings.append({"severity": "medium", "issue": "Deadlock retries have no backoff strategy."})
    if transaction.get("deadlock_rate_per_hour", 0) > transaction.get("max_acceptable_deadlock_rate", 10):
        findings.append({"severity": "high", "issue": "Deadlock rate exceeds the acceptable threshold, suggesting a lock-ordering issue."})
    return findings
