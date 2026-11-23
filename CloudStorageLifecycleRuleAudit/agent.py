"""Flags cloud storage buckets that store logs but have no lifecycle rule configured, letting log data accumulate and cost grow unbounded forever."""
from typing import Any


def audit(bucket: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if bucket.get("stores_logs") and not bucket.get("lifecycle_rules_configured"):
        findings.append({"severity": "medium", "issue": "Bucket stores logs but has no lifecycle rule to expire or transition old objects."})
    return findings
