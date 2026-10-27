"""Check secret inventory for expiry and rotation monitoring coverage."""
from typing import Any


def audit(secret: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if secret.get("expires_on") is None and not secret.get("rotation_policy"):
        findings.append({"severity": "high", "issue": "Secret has neither an expiry date nor a rotation policy."})
    if secret.get("days_until_expiry", 99999) <= secret.get("warning_window_days", 30) and not secret.get("rotation_started"):
        findings.append({"severity": "high", "issue": "Secret is near expiry but rotation has not started."})
    if not secret.get("expiry_alert_configured"):
        findings.append({"severity": "medium", "issue": "No alert is configured for secret expiry."})
    if secret.get("owner_active") is False and not secret.get("ownership_transferred"):
        findings.append({"severity": "medium", "issue": "Secret owner is inactive and ownership is not transferred."})
    return findings
