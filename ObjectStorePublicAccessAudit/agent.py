"""Audit object-storage exposure, policy scope, and access logging."""
from typing import Any


def audit(bucket: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if bucket.get("public_access"):
        findings.append({"severity": "critical", "issue": "Bucket permits public access."})
    if bucket.get("policy_principal") == "*" and not bucket.get("public_access_exception_approved"):
        findings.append({"severity": "high", "issue": "Wildcard policy principal lacks an approved exception."})
    if bucket.get("sensitive_data") and not bucket.get("access_logging"):
        findings.append({"severity": "high", "issue": "Sensitive bucket has no access logging."})
    if not bucket.get("encryption"):
        findings.append({"severity": "high", "issue": "At-rest encryption is not confirmed."})
    return findings
