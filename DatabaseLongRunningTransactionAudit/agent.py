"""Flags database transactions open longer than acceptable, risking lock contention and bloat."""
from typing import Any


def audit(transaction: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if transaction.get("duration_seconds", 0) > transaction.get("max_acceptable_duration_seconds", 60):
        findings.append({"severity": "high", "issue": "Transaction has been open longer than the acceptable duration."})
    if transaction.get("holds_locks") and transaction.get("duration_seconds", 0) > 30:
        findings.append({"severity": "medium", "issue": "Long-running transaction is holding locks."})
    return findings
