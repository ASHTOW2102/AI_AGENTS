"""Flags database tables with rows whose foreign key no longer resolves to an existing parent row, indicating a missing or disabled constraint."""
from typing import Any


def audit(table: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if table.get("orphaned_row_count", 0) > 0:
        findings.append({"severity": "high", "issue": f"{table.get('orphaned_row_count')} rows reference a non-existent parent row."})
    if not table.get("foreign_key_constraint_enforced"):
        findings.append({"severity": "medium", "issue": "Foreign key constraint is not enforced at the database level."})
    return findings
