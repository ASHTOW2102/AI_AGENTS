"""Check backup schedule coverage for critical systems and retention windows."""
from typing import Any


def audit(system: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if system.get("critical") and not system.get("backup_schedule"):
        findings.append({"severity": "critical", "issue": "Critical system has no scheduled backup."})
    if system.get("backup_interval_hours", 0) > system.get("max_backup_interval_hours", 0):
        findings.append({"severity": "high", "issue": "Backup interval exceeds the approved maximum."})
    if system.get("retention_days", 0) < system.get("minimum_retention_days", 0):
        findings.append({"severity": "medium", "issue": "Backup retention is shorter than the required minimum."})
    if not system.get("last_backup_success"):
        findings.append({"severity": "high", "issue": "Most recent backup is not confirmed successful."})
    return findings
