"""Review object-lock retention schedules and legal-hold evidence."""
from typing import Any


def audit(lock: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not lock.get("retention_mode"):
        findings.append({"severity": "high", "issue": "Object lock retention mode is not configured."})
    if lock.get("retention_days", 0) < lock.get("required_retention_days", 0):
        findings.append({"severity": "high", "issue": "Object retention period is shorter than required."})
    if lock.get("legal_hold_required") and not lock.get("legal_hold_confirmed"):
        findings.append({"severity": "high", "issue": "Required legal hold is not confirmed."})
    if lock.get("bypass_permission_count", 0) > 0:
        findings.append({"severity": "medium", "issue": "One or more principals can bypass retention controls."})
    return findings
