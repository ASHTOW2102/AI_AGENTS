"""Flags storage buckets holding compliance records with no object lock configured, so records can be deleted or altered before their legal retention period ends."""
from typing import Any


def audit(bucket: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if bucket.get("stores_compliance_records") and not bucket.get("object_lock_enabled"):
        findings.append({"severity": "high", "issue": "Bucket stores compliance records but has no object lock configured."})
    return findings
