"""Flags foreign keys with ON DELETE CASCADE pointing at financial or audit data, where a single parent delete can silently wipe out records that must be retained."""
from typing import Any


def audit(foreign_key: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if foreign_key.get("references_financial_data") and foreign_key.get("on_delete") == "CASCADE":
        findings.append({"severity": "high", "issue": "Foreign key cascades deletes into financial/audit data."})
    return findings
