"""Flags state-changing endpoints with no CSRF protection at all, or whose CSRF token is never validated against the current session."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("csrf_protection_enabled"):
        findings.append({"severity": "high", "issue": "State-changing endpoint has no CSRF protection."})
    elif not endpoint.get("validates_token_against_session"):
        findings.append({"severity": "medium", "issue": "CSRF token is accepted without being validated against the current session."})
    return findings
