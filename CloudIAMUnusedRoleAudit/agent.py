"""Flags cloud IAM roles that have been unused for an extended period and should be revoked."""
from typing import Any


def audit(role: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if role.get("days_since_last_use", 0) > role.get("max_acceptable_unused_days", 90):
        findings.append({"severity": "medium", "issue": "Role has not been used within the acceptable window."})
    if role.get("days_since_last_use", 0) > 365 and role.get("grants_admin_access"):
        findings.append({"severity": "high", "issue": "Unused admin-granting role has not been reviewed in over a year."})
    return findings
