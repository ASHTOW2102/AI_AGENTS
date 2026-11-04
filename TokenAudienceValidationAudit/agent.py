"""Checks that services validate token audience claims and reject tokens minted for other services."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not service.get("validates_audience_claim"):
        findings.append({"severity": "critical", "issue": "Service does not validate the token audience claim."})
    if service.get("validates_audience_claim") and service.get("accepts_wildcard_audience"):
        findings.append({"severity": "high", "issue": "Audience validation accepts a wildcard value."})
    if service.get("shares_signing_key_with_other_services") and not service.get("validates_audience_claim"):
        findings.append({"severity": "critical", "issue": "Shared signing key with no audience check allows cross-service token replay."})
    return findings
