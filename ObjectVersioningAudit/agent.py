"""Review object versioning policy for recovery and lifecycle evidence."""
from typing import Any


def audit(bucket: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if bucket.get("versioning_required") and not bucket.get("versioning_enabled"):
        findings.append({"severity": "high", "issue": "Required object versioning is disabled."})
    if bucket.get("versioning_enabled") and not bucket.get("delete_marker_recovery_tested"):
        findings.append({"severity": "medium", "issue": "Recovery from accidental deletion has not been tested."})
    if bucket.get("versioning_enabled") and not bucket.get("noncurrent_version_lifecycle"):
        findings.append({"severity": "low", "issue": "Noncurrent object versions have no lifecycle policy."})
    if bucket.get("versioning_enabled") and not bucket.get("mfa_delete_or_equivalent") and bucket.get("critical_data"):
        findings.append({"severity": "medium", "issue": "Critical versioned data has no stronger delete safeguard."})
    return findings
