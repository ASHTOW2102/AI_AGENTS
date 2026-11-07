"""Flags database queries with no statement timeout, risking long-held locks on slow queries."""
from typing import Any


def audit(query: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not query.get("statement_timeout_ms"):
        findings.append({"severity": "high", "issue": "Query has no statement timeout configured."})
    if query.get("statement_timeout_ms") and query.get("statement_timeout_ms", 0) > query.get("max_acceptable_timeout_ms", 30000):
        findings.append({"severity": "medium", "issue": "Statement timeout exceeds the acceptable threshold."})
    return findings
