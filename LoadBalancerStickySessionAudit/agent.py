"""Flags load balancers using sticky sessions with an unencrypted session cookie, exposing the session-routing identifier in plaintext."""
from typing import Any


def audit(lb: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if lb.get("sticky_sessions_enabled") and not lb.get("session_cookie_encrypted"):
        findings.append({"severity": "medium", "issue": "Sticky sessions are enabled with an unencrypted session cookie."})
    return findings
