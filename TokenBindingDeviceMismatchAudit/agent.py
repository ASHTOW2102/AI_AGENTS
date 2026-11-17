"""Flags sessions where the authentication token is used from a device fingerprint different from the one it was issued to."""
from typing import Any


def audit(session: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if session.get("token_bound_to_device") and session.get("current_device_fingerprint") != session.get("issued_device_fingerprint"):
        findings.append({"severity": "high", "issue": "Token is being used from a device fingerprint different from the one it was issued to."})
    if not session.get("token_bound_to_device"):
        findings.append({"severity": "medium", "issue": "Token is not bound to a device fingerprint at all."})
    return findings
