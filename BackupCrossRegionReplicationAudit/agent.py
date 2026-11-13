"""Flags backups stored only in their primary region without cross-region replication for disaster recovery."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not backup.get("cross_region_replicated"):
        findings.append({"severity": "high", "issue": "Backup is not replicated to a secondary region."})
    if backup.get("cross_region_replicated") and backup.get("replication_lag_hours", 0) > backup.get("max_acceptable_lag_hours", 24):
        findings.append({"severity": "medium", "issue": "Cross-region replication lag exceeds the acceptable threshold."})
    return findings
