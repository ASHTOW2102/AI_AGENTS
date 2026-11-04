"""Checks long-running database queries for statement timeouts and lock-contention impact."""
from typing import Any


def audit(query: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not query.get("statement_timeout_configured"):
        findings.append({"severity": "high", "issue": "Query has no statement timeout configured."})
    if query.get("duration_seconds", 0) > query.get("max_acceptable_duration_seconds", 30) and query.get("holds_locks"):
        findings.append({"severity": "high", "issue": "Long-running query holds locks well beyond the acceptable duration."})
    if query.get("runs_on_primary") and query.get("read_only") and not query.get("could_run_on_replica"):
        findings.append({"severity": "low", "issue": "Read-only long query runs on the primary though a replica could serve it."})
    return findings
