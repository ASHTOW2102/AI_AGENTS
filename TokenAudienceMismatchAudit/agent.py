"""Flags tokens accepted by a service whose audience claim does not match that service's identifier."""
from typing import Any


def audit(token: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if token.get("audience_claim") != token.get("expected_service_id"):
        findings.append({"severity": "high", "issue": "Token audience claim does not match the expected service identifier."})
    if not token.get("audience_validated"):
        findings.append({"severity": "high", "issue": "Service does not validate the token audience claim at all."})
    return findings
