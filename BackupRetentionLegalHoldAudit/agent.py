"""Checks backups under legal hold are excluded from routine deletion and retention-expiry jobs."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if backup.get("legal_hold_active") and backup.get("eligible_for_scheduled_deletion"):
        findings.append({"severity": "critical", "issue": "Backup under legal hold is still eligible for scheduled deletion."})
    if backup.get("legal_hold_active") and not backup.get("legal_hold_reference"):
        findings.append({"severity": "medium", "issue": "Legal hold has no case or matter reference recorded."})
    if backup.get("legal_hold_released") and backup.get("deletion_resumed_days_ago", 0) > 30:
        findings.append({"severity": "low", "issue": "Deletion did not resume promptly after the legal hold was released."})
    return findings
