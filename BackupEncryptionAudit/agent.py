"""Audit encryption and key-management settings for backup archives."""
from __future__ import annotations

from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not backup.get("encrypted"):
        findings.append({"severity": "critical", "issue": "Backup data is not encrypted."})
    if backup.get("key_type") != "managed_kms":
        findings.append({"severity": "high", "issue": "Backup encryption key is not managed by an approved KMS."})
    if backup.get("key_rotation_days", 0) > 365:
        findings.append({"severity": "medium", "issue": "Encryption key rotation interval exceeds one year."})
    if backup.get("key_stored_with_backup"):
        findings.append({"severity": "critical", "issue": "Encryption key is stored alongside the backup."})
    if backup.get("restore_access_count", 0) > backup.get("approved_restore_access_count", 0):
        findings.append({"severity": "medium", "issue": "Restore access exceeds the approved principal count."})
    return findings
