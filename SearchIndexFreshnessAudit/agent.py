"""Flags search indexes with stale documents exceeding the acceptable reindex lag."""
from typing import Any


def audit(index: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if index.get("reindex_lag_seconds", 0) > index.get("max_acceptable_lag_seconds", 300):
        findings.append({"severity": "medium", "issue": "Search index reindex lag exceeds the acceptable threshold."})
    if index.get("failed_reindex_count", 0) > 0:
        findings.append({"severity": "high", "issue": "There are unresolved failed reindex attempts."})
    return findings
