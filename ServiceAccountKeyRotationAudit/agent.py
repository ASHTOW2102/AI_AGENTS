"""Flags service account credentials (API keys, static JSON keys) with no rotation policy or with an age exceeding the organization's rotation window."""
from typing import Any


def audit(account: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    has_rotation_policy = account.get("has_rotation_policy", False)
    age_days = account.get("key_age_days", 0)
    max_age_days = account.get("max_allowed_age_days", 90)

    if not has_rotation_policy:
        findings.append({"severity": "high", "issue": "Service account key has no rotation policy, so a leaked credential remains valid indefinitely."})
    if age_days > max_age_days:
        findings.append({"severity": "medium", "issue": f"Service account key is {age_days} days old, exceeding the {max_age_days}-day rotation window."})
    return findings
