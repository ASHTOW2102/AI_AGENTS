"""Checks cloud storage buckets for disabled versioning that would prevent recovery from accidental overwrite or deletion."""
from typing import Any


def audit(bucket: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not bucket.get("versioning_enabled"):
        findings.append({"severity": "high", "issue": "Bucket versioning is disabled, risking unrecoverable overwrites."})
    if bucket.get("versioning_enabled") and not bucket.get("lifecycle_policy_configured"):
        findings.append({"severity": "low", "issue": "Versioning enabled but no lifecycle policy to expire old versions."})
    return findings
