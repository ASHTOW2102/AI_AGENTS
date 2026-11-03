"""Checks outbound network proxy allowlists for overly broad or stale destination rules."""
from typing import Any


def audit(proxy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if proxy.get("allows_wildcard_destination"):
        findings.append({"severity": "high", "issue": "Outbound proxy allows a wildcard destination rule."})
    if proxy.get("unused_rule_days", 0) > proxy.get("max_unused_rule_days", 180):
        findings.append({"severity": "low", "issue": "An allowlist rule has been unused beyond the review window."})
    if proxy.get("destination_requires_tls") is False and proxy.get("destination_handles_sensitive_data"):
        findings.append({"severity": "high", "issue": "Allowlisted destination handling sensitive data does not require TLS."})
    return findings
