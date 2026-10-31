"""Review backup restore permissions and separation of duties."""
from typing import Any


def audit(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if policy.get("restore_permission_count", 0) > policy.get("approved_restore_permission_count", 0):
        findings.append({"severity": "medium", "issue": "Restore access exceeds the approved principal count."})
    if policy.get("restore_admins_overlap_delete_admins"):
        findings.append({"severity": "high", "issue": "Restore operators can also delete backup copies."})
    if policy.get("restore_to_production_allowed") and not policy.get("restore_requires_approval"):
        findings.append({"severity": "high", "issue": "Production restore can proceed without approval."})
    if not policy.get("restore_activity_logged"):
        findings.append({"severity": "low", "issue": "Backup restore activity is not logged."})
    return findings
