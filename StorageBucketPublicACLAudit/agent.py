"""Flags cloud storage buckets with a public-read ACL, at high severity when the bucket is also known to contain sensitive data."""
from typing import Any


def audit(bucket: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if bucket.get("public_read_acl"):
        severity = "high" if bucket.get("contains_sensitive_data") else "medium"
        findings.append({"severity": severity, "issue": "Bucket has a public-read ACL."})
    return findings
