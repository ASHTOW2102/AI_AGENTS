"""Checks backup encryption keys for overdue rotation and insecure storage of the active key."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if backup.get("key_age_days", 0) > backup.get("max_key_age_days", 365):
        findings.append({"severity": "high", "issue": "Backup encryption key exceeds the maximum rotation age."})
    if backup.get("key_stored_alongside_backup"):
        findings.append({"severity": "high", "issue": "Encryption key is stored alongside the backup it protects."})
    return findings
