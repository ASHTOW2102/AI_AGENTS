"""Flags inbound connections originating from ASNs with poor reputation scores that bypass blocking rules."""
from typing import Any


def audit(connection: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if connection.get("source_asn_reputation_score", 100) < connection.get("min_acceptable_reputation_score", 40) and not connection.get("blocked"):
        findings.append({"severity": "high", "issue": "Low-reputation ASN traffic was not blocked."})
    if not connection.get("asn_reputation_checked"):
        findings.append({"severity": "medium", "issue": "Source ASN reputation is not checked at all."})
    return findings
