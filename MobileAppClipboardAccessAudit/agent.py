"""Flags mobile apps that copy sensitive data to the system clipboard without clearing it after a timeout, leaving it readable by any other app."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("copies_sensitive_data_to_clipboard") and not app.get("clears_clipboard_after_timeout"):
        findings.append({"severity": "high", "issue": "Sensitive data is copied to the clipboard and never cleared, readable by any other app."})
    return findings
