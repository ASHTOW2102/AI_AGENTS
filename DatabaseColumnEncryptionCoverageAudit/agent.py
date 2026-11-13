"""Flags database tables with sensitive columns that are not covered by column-level encryption."""
from typing import Any


def audit(table: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    unencrypted = [c for c in table.get("sensitive_columns", []) if c not in table.get("encrypted_columns", [])]
    if unencrypted:
        findings.append({"severity": "high", "issue": f"Sensitive columns without encryption: {unencrypted}"})
    if table.get("encrypted_columns") and not table.get("key_managed_by_kms"):
        findings.append({"severity": "medium", "issue": "Encrypted columns use keys not managed by a KMS."})
    return findings
