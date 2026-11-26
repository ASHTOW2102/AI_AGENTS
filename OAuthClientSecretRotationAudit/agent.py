"""Flags OAuth client secrets that have gone unrotated past their own configured maximum rotation interval."""
from typing import Any


def audit(client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    last_rotated = client.get("secret_last_rotated_days_ago", 0)
    max_interval = client.get("max_rotation_interval_days", 0)
    if max_interval and last_rotated > max_interval:
        findings.append({"severity": "medium", "issue": f"OAuth client secret last rotated {last_rotated} days ago, past its {max_interval}-day interval."})
    return findings
