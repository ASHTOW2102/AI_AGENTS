"""Review WebSocket authentication expiry and long-lived connection renewal."""
from typing import Any


def audit(connection: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if connection.get("auth_expires_during_connection") and not connection.get("reauthentication_supported"):
        findings.append({"severity": "high", "issue": "WebSocket cannot reauthenticate after credentials expire."})
    if connection.get("reauthentication_supported") and not connection.get("reauthentication_deadline_enforced"):
        findings.append({"severity": "medium", "issue": "Reauthentication has no enforced deadline."})
    if connection.get("revocation_required") and not connection.get("active_connections_closed_on_revocation"):
        findings.append({"severity": "high", "issue": "Revoked credentials do not close existing connections."})
    if connection.get("max_connection_age_hours", 0) > connection.get("approved_max_connection_age_hours", 24):
        findings.append({"severity": "low", "issue": "Maximum WebSocket connection age exceeds policy."})
    return findings
