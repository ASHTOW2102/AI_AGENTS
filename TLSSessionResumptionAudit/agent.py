"""Flags TLS servers supporting session resumption whose session ticket keys are never rotated, letting a single leaked key decrypt sessions indefinitely."""
from typing import Any


def audit(server: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if server.get("supports_session_resumption") and not server.get("session_ticket_key_rotation_enabled"):
        findings.append({"severity": "medium", "issue": "Session resumption is supported but ticket keys are never rotated."})
    return findings
