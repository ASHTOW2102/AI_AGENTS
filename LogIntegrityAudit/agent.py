"""Review centralized log integrity, access, and retention safeguards."""
from typing import Any


def audit(log_policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not log_policy.get("tamper_protection"):
        findings.append({"severity": "high", "issue": "Log storage has no tamper-protection control."})
    if not log_policy.get("access_audited"):
        findings.append({"severity": "medium", "issue": "Access to log data is not audited."})
    if log_policy.get("retention_days", 0) < log_policy.get("minimum_retention_days", 0):
        findings.append({"severity": "medium", "issue": "Log retention is shorter than the required minimum."})
    if log_policy.get("admin_write_access") and not log_policy.get("separate_admin_domain"):
        findings.append({"severity": "high", "issue": "Log administrators share the production identity domain."})
    return findings
