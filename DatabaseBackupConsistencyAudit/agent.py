"""Check database backup consistency and recovery evidence metadata."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if backup.get("multi_volume") and not backup.get("snapshot_group_consistent"):
        findings.append({"severity": "high", "issue": "Multi-volume backup is not captured as a consistent snapshot group."})
    if backup.get("transactional_database") and not backup.get("log_position_recorded"):
        findings.append({"severity": "medium", "issue": "Database backup lacks a transaction-log recovery position."})
    if not backup.get("integrity_check_passed"):
        findings.append({"severity": "high", "issue": "Backup integrity verification is not confirmed."})
    if not backup.get("restore_tested"):
        findings.append({"severity": "medium", "issue": "Backup has no recorded restore test."})
    return findings
