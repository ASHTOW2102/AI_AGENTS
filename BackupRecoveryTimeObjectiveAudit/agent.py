"""Flags backup/restore procedures whose measured recovery time exceeds the business's recovery time objective."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if backup.get("measured_restore_time_minutes", 0) > backup.get("rto_minutes", 60):
        findings.append({"severity": "high", "issue": "Measured restore time exceeds the recovery time objective."})
    if not backup.get("restore_tested_within_last_quarter"):
        findings.append({"severity": "medium", "issue": "Restore procedure has not been tested in the last quarter."})
    return findings
