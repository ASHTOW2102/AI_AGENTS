"""Flags web applications that keep the same session identifier across login, letting an attacker fixate a victim's session before authentication."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not app.get("session_id_rotated_on_login"):
        findings.append({"severity": "high", "issue": "Session identifier is not rotated after successful login, enabling session fixation."})
    if not app.get("session_id_rotated_on_privilege_change"):
        findings.append({"severity": "medium", "issue": "Session identifier is not rotated on privilege escalation (e.g. becoming admin)."})
    return findings
