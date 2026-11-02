"""Checks database connection pool metrics for leaked or long-held connections."""
from typing import Any


def audit(pool: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pool.get("active_connections", 0) >= pool.get("pool_size", 0) and pool.get("growth_trend") == "increasing":
        findings.append({"severity": "high", "issue": "Active connections are saturating the pool with an increasing trend."})
    if pool.get("longest_held_connection_minutes", 0) > pool.get("max_expected_hold_minutes", 5):
        findings.append({"severity": "medium", "issue": "A connection has been held far longer than expected."})
    if pool.get("connections_without_explicit_close", 0) > 0:
        findings.append({"severity": "medium", "issue": "Connections are closing via timeout rather than explicit release."})
    return findings
