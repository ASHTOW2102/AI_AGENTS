"""Compare data-class retention schedules to policy and deletion evidence."""
from typing import Any


def audit(record: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if record.get("retention_days", 0) > record.get("policy_max_days", 0):
        findings.append({"severity": "high", "issue": "Configured retention exceeds the policy maximum."})
    if record.get("deletion_due") and not record.get("deletion_job_enabled"):
        findings.append({"severity": "high", "issue": "Deletion is due but no deletion job is enabled."})
    if record.get("deletion_job_enabled") and not record.get("deletion_evidence_retained"):
        findings.append({"severity": "medium", "issue": "Deletion job has no retained completion evidence."})
    if record.get("legal_hold") and record.get("deletion_due"):
        findings.append({"severity": "low", "issue": "Deletion due date should be reviewed against active legal hold."})
    return findings
