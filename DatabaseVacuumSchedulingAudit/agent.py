"""Flags database tables with autovacuum disabled or badly tuned, risking bloat and transaction ID wraparound."""
from typing import Any


def audit(table: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not table.get("autovacuum_enabled"):
        findings.append({"severity": "high", "issue": "Autovacuum is disabled on this table."})
    if table.get("dead_tuple_ratio", 0) > table.get("max_acceptable_dead_tuple_ratio", 0.2):
        findings.append({"severity": "medium", "issue": "Dead tuple ratio exceeds the acceptable threshold."})
    return findings
