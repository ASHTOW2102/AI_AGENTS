"""Flags mobile apps that copy sensitive data to the system clipboard without expiry or exclusion from clipboard history."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("copies_sensitive_data_to_clipboard") and not app.get("clipboard_auto_expire_enabled"):
        findings.append({"severity": "high", "issue": "Sensitive data copied to clipboard has no auto-expiry."})
    if app.get("copies_sensitive_data_to_clipboard") and not app.get("excluded_from_clipboard_history"):
        findings.append({"severity": "medium", "issue": "Sensitive clipboard content is not excluded from clipboard history."})
    return findings
