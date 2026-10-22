"""Review backup immutability and administrative separation controls."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not backup.get("immutable"):
        findings.append({"severity": "high", "issue": "Backup has no immutability or write-once protection."})
    if backup.get("immutability_days", 0) < backup.get("required_immutability_days", 0):
        findings.append({"severity": "medium", "issue": "Immutability period is shorter than the required minimum."})
    if backup.get("delete_admins_overlap_production_admins"):
        findings.append({"severity": "high", "issue": "Backup deletion administrators overlap production administrators."})
    if not backup.get("restore_tested"):
        findings.append({"severity": "medium", "issue": "Immutable backup restore has not been tested."})
    return findings
