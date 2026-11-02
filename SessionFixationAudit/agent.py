"""Checks authentication flows for session-ID rotation on login and privilege change."""
from typing import Any


def audit(flow: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not flow.get("session_id_rotated_on_login"):
        findings.append({"severity": "high", "issue": "Session ID is not rotated on successful login."})
    if flow.get("privilege_change_possible") and not flow.get("session_id_rotated_on_privilege_change"):
        findings.append({"severity": "high", "issue": "Session ID is not rotated when privilege level changes."})
    if flow.get("pre_login_session_accepted_after_login"):
        findings.append({"severity": "critical", "issue": "A pre-login session ID remains valid after authentication."})
    return findings
