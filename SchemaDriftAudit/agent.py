"""Compares live table schemas with declared data-model definitions to catch undocumented drift."""
from typing import Any


def audit(table: dict[str, Any]):
    findings = []
    extra = sorted(set(table.get("live_columns", [])) - set(table.get("declared_columns", [])))
    if extra:
        findings.append({"severity": "high", "issue": "Undocumented columns present: " + ", ".join(extra)})
    missing = sorted(set(table.get("declared_columns", [])) - set(table.get("live_columns", [])))
    if missing:
        findings.append({"severity": "high", "issue": "Declared columns missing from live schema: " + ", ".join(missing)})
    if table.get("type_mismatches"):
        findings.append({"severity": "medium", "issue": "Column type mismatches detected between declaration and live schema."})
    return findings
