"""Flags cloud KMS key grants that have no expiry set, leaving indefinite decrypt or sign access."""
from typing import Any


def audit(grant: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not grant.get("expiry_set"):
        findings.append({"severity": "high", "issue": "KMS grant has no expiry set."})
    if grant.get("expiry_set") and grant.get("expiry_days", 0) > grant.get("max_acceptable_expiry_days", 90):
        findings.append({"severity": "medium", "issue": "KMS grant expiry exceeds the acceptable maximum duration."})
    return findings
