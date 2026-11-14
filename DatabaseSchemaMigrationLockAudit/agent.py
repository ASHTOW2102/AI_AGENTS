"""Flags database schema migrations that take exclusive table locks on large tables during business hours."""
from typing import Any


def audit(migration: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if migration.get("takes_exclusive_lock") and migration.get("table_row_count", 0) > migration.get("large_table_threshold", 1000000):
        findings.append({"severity": "high", "issue": "Migration takes an exclusive lock on a large table."})
    if migration.get("takes_exclusive_lock") and migration.get("scheduled_during_business_hours"):
        findings.append({"severity": "medium", "issue": "Lock-taking migration is scheduled during business hours."})
    return findings
