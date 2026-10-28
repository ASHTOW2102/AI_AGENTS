"""Review mobile clipboard exposure of sensitive app content."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("sensitive_fields_copyable") and not app.get("clipboard_expiry"):
        findings.append({"severity": "medium", "issue": "Sensitive copied content has no clipboard expiry or clearing policy."})
    if app.get("auth_secrets_copyable"):
        findings.append({"severity": "high", "issue": "Authentication secrets can be copied to the system clipboard."})
    if app.get("clipboard_access_logged") and app.get("clipboard_content_logged"):
        findings.append({"severity": "critical", "issue": "Clipboard content itself is recorded in logs."})
    if app.get("sensitive_fields_copyable") and not app.get("copy_warning_or_confirmation"):
        findings.append({"severity": "low", "issue": "Copying sensitive values has no user warning or confirmation."})
    return findings
