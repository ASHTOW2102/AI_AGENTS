"""Checks foreign-key relationships for enforcement and orphaned-row risk across related tables."""
from typing import Any


def audit(table: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if table.get("logical_fk_count", 0) > 0 and not table.get("fk_constraint_enforced"):
        findings.append({"severity": "high", "issue": "Logical foreign-key relationships are not enforced by database constraints."})
    if table.get("orphaned_row_count", 0) > 0:
        findings.append({"severity": "high", "issue": "Orphaned rows reference a parent that no longer exists."})
    if table.get("fk_constraint_enforced") and table.get("cascade_delete_enabled") and not table.get("cascade_delete_reviewed"):
        findings.append({"severity": "medium", "issue": "Cascading delete is enabled without a documented review."})
    return findings
