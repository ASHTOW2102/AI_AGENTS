"""Measures how long revoked tokens remain usable due to propagation delay in validation caches."""
from typing import Any


def audit(token: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if token.get("revocation_propagation_ms", 0) > token.get("max_acceptable_propagation_ms", 5000):
        findings.append({"severity": "high", "issue": "Revocation propagation delay exceeds the acceptable threshold."})
    if not token.get("revocation_checked_on_validate"):
        findings.append({"severity": "high", "issue": "Token validation does not check the revocation list at all."})
    return findings
