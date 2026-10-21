"""Check backup restore drills for recency, coverage, and objective evidence."""
from typing import Any


def audit(drill: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if drill.get("days_since_last_restore", 0) > drill.get("max_days_between_drills", 365):
        findings.append({"severity": "high", "issue": "Restore drill is overdue."})
    if drill.get("critical_datasets", 0) > drill.get("datasets_restored", 0):
        findings.append({"severity": "high", "issue": "Restore drill did not cover all critical datasets."})
    if drill.get("measured_rto_minutes", 0) > drill.get("target_rto_minutes", 0):
        findings.append({"severity": "high", "issue": "Measured restore time exceeded the RTO target."})
    if not drill.get("integrity_verified"):
        findings.append({"severity": "medium", "issue": "Restored data integrity was not verified."})
    if not drill.get("evidence_reference"):
        findings.append({"severity": "low", "issue": "No evidence reference is recorded for the drill."})
    return findings
