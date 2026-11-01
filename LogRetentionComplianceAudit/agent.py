"""Checks log retention duration and deletion evidence against compliance requirements."""
from typing import Any


def audit(log_source: dict[str, Any]):
    findings = []
    if log_source.get("retention_days", 0) < log_source.get("required_retention_days", 0):
        findings.append({"severity": "high", "issue": "Log retention is shorter than the compliance requirement."})
    if log_source.get("contains_pii") and log_source.get("retention_days", 0) > log_source.get("max_pii_retention_days", 0):
        findings.append({"severity": "high", "issue": "PII logs are retained beyond the allowed maximum."})
    if not log_source.get("deletion_job_verified"):
        findings.append({"severity": "medium", "issue": "Log deletion job has no verification evidence."})
    return findings
