"""Flags database tables whose query-planner statistics are stale relative to the volume of changes since the last analyze."""
from typing import Any


def audit(table: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if table.get("rows_changed_since_analyze", 0) > table.get("row_count", 1) * table.get("max_acceptable_change_fraction", 0.1):
        findings.append({"severity": "medium", "issue": "Rows changed since last ANALYZE exceed the acceptable fraction, risking a stale query plan."})
    if not table.get("auto_analyze_enabled"):
        findings.append({"severity": "low", "issue": "Automatic statistics refresh is not enabled for this table."})
    return findings
