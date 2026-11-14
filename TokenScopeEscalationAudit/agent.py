"""Flags token issuance flows that allow a client to request broader scopes than it was originally registered for."""
from typing import Any


def audit(token: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    excess = set(token.get("requested_scopes", [])) - set(token.get("registered_scopes", []))
    if excess:
        findings.append({"severity": "high", "issue": f"Client requested scopes beyond its registration: {sorted(excess)}"})
    if not token.get("scope_validated_at_issuance"):
        findings.append({"severity": "high", "issue": "Token issuance does not validate requested scopes at all."})
    return findings
