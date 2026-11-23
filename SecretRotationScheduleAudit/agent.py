"""Flags secrets that have gone unrotated past their own configured maximum rotation interval."""
from typing import Any


def audit(secret: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    last_rotated = secret.get("last_rotated_days_ago", 0)
    max_interval = secret.get("max_rotation_interval_days", 0)
    if max_interval and last_rotated > max_interval:
        findings.append({"severity": "medium", "issue": f"Secret was last rotated {last_rotated} days ago, past its {max_interval}-day rotation interval."})
    return findings
