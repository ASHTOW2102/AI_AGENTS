"""Flags databases that retry deadlocked transactions with no backoff, so a deadlock under load triggers a self-reinforcing retry storm."""
from typing import Any


def audit(db: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if db.get("deadlock_retry_enabled") and not db.get("retry_backoff_configured"):
        findings.append({"severity": "high", "issue": "Deadlock retries are enabled with no backoff, risking a retry storm under load."})
    return findings
