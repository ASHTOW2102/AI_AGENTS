"""Checks mobile push-token registration lifecycle for staleness and revocation handling."""
from typing import Any


def audit(registration: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if registration.get("age_days", 0) > registration.get("max_valid_age_days", 270):
        findings.append({"severity": "medium", "issue": "Push token has exceeded its expected validity window."})
    if registration.get("delivery_failures_in_a_row", 0) >= 3 and not registration.get("token_invalidated"):
        findings.append({"severity": "medium", "issue": "Repeated delivery failures did not invalidate the token."})
    if registration.get("user_logged_out") and not registration.get("token_unregistered"):
        findings.append({"severity": "high", "issue": "Token remains registered after user logout."})
    return findings
