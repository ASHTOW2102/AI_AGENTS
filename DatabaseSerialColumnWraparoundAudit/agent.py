"""Flags database serial/auto-increment columns approaching their integer type's maximum value with no migration planned."""
from typing import Any


def audit(column: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    utilization = column.get("current_value", 0) / column.get("max_value_for_type", 1)
    if utilization > column.get("max_acceptable_utilization", 0.8):
        findings.append({"severity": "high", "issue": "Serial column is approaching its integer type's maximum value."})
    if utilization > column.get("max_acceptable_utilization", 0.8) and not column.get("migration_to_larger_type_planned"):
        findings.append({"severity": "high", "issue": "No migration to a larger integer type is planned despite nearing wraparound."})
    return findings
