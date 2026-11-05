"""Checks sensitive mobile operations for device-attestation checks against rooted or tampered devices."""
from typing import Any


def audit(session: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if session.get("operation_sensitive") and not session.get("device_attestation_checked"):
        findings.append({"severity": "high", "issue": "Sensitive operation runs with no device attestation check."})
    if session.get("device_rooted_or_jailbroken") and session.get("operation_allowed"):
        findings.append({"severity": "high", "issue": "Operation was allowed to proceed on a rooted or jailbroken device."})
    if session.get("attestation_token_cached_minutes", 0) > session.get("max_attestation_cache_minutes", 60):
        findings.append({"severity": "medium", "issue": "Attestation result is cached longer than the recommended window."})
    return findings
