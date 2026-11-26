"""Flags database backups that are not encrypted at rest, leaving a full data copy exposed if the backup storage is ever breached."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not backup.get("encrypted_at_rest"):
        findings.append({"severity": "high", "issue": "Database backup is not encrypted at rest."})
    return findings
