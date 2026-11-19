"""Flags load balancers using sticky sessions keyed on a predictable cookie value, letting an attacker pin victims to an attacker-controlled backend."""
from typing import Any


def audit(lb: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if lb.get("sticky_sessions_enabled") and lb.get("session_cookie_value_predictable"):
        findings.append({"severity": "high", "issue": "Sticky session cookie value is predictable, allowing session pinning attacks."})
    if lb.get("sticky_sessions_enabled") and not lb.get("session_cookie_signed"):
        findings.append({"severity": "medium", "issue": "Sticky session cookie is not signed, allowing tampering with the routing decision."})
    return findings
