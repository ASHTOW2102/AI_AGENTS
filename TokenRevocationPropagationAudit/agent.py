"""Checks that revoked access tokens stop working promptly across all validating services."""
from typing import Any


def audit(system: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if system.get("revocation_propagation_seconds", 0) > system.get("max_acceptable_propagation_seconds", 60):
        findings.append({"severity": "high", "issue": "Revoked tokens remain valid at some services longer than acceptable."})
    if system.get("token_type") == "jwt" and not system.get("revocation_checked_against_denylist"):
        findings.append({"severity": "high", "issue": "Stateless JWTs are not checked against a revocation denylist."})
    if system.get("cached_validation_results") and system.get("cache_ttl_seconds", 0) > system.get("max_acceptable_propagation_seconds", 60):
        findings.append({"severity": "medium", "issue": "Cached token validation results outlive the acceptable revocation window."})
    return findings
