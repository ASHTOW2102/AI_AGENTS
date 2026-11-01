"""Checks that backups replicate to a separate region and verifies restore evidence there."""
from typing import Any


def audit(backup: dict[str, Any]):
    findings = []
    if not backup.get("cross_region_copy_exists"):
        findings.append({"severity": "high", "issue": "Backup has no cross-region copy."})
    if backup.get("cross_region_copy_exists") and backup.get("replication_lag_hours", 0) > backup.get("max_replication_lag_hours", 24):
        findings.append({"severity": "medium", "issue": "Cross-region backup replication lag exceeds policy."})
    if not backup.get("cross_region_restore_tested"):
        findings.append({"severity": "high", "issue": "Cross-region restore has not been tested."})
    return findings
