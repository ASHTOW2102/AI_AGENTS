"""Flags mobile apps whose background refresh tasks continue fetching sensitive data after the user has logged out."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("has_background_refresh") and not app.get("background_refresh_cancelled_on_logout"):
        findings.append({"severity": "high", "issue": "Background refresh is not cancelled when the user logs out, risking data fetched for a signed-out session."})
    if app.get("has_background_refresh") and not app.get("background_fetch_requires_valid_session"):
        findings.append({"severity": "medium", "issue": "Background fetch does not validate the session is still active before running."})
    return findings
