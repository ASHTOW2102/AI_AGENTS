"""Flags data warehouse columns containing PII that are not tagged for access control and masking policies."""
from typing import Any


def audit(table: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    untagged = [c for c in table.get("pii_columns", []) if c not in table.get("tagged_columns", [])]
    if untagged:
        findings.append({"severity": "high", "issue": f"PII columns not tagged for access control: {untagged}"})
    if table.get("pii_columns") and not table.get("masking_policy_applied"):
        findings.append({"severity": "medium", "issue": "Table contains PII but has no masking policy applied."})
    return findings
