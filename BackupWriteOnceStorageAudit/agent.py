"""Flags backups stored on mutable storage instead of write-once-read-many storage, risking ransomware tampering."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not backup.get("worm_storage_enabled"):
        findings.append({"severity": "high", "issue": "Backup is not stored on write-once-read-many storage."})
    if backup.get("worm_storage_enabled") and backup.get("retention_lock_days", 0) < backup.get("min_required_lock_days", 30):
        findings.append({"severity": "medium", "issue": "WORM retention lock is shorter than the required minimum."})
    return findings
