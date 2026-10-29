"""Review WebAuthn challenge freshness and origin validation controls."""
from typing import Any


def audit(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if policy.get("challenge_ttl_seconds", 0) > policy.get("max_challenge_ttl_seconds", 300):
        findings.append({"severity": "medium", "issue": "Authentication challenge lifetime exceeds policy."})
    if not policy.get("challenge_single_use"):
        findings.append({"severity": "high", "issue": "WebAuthn challenge can be reused."})
    if not policy.get("origin_validation"):
        findings.append({"severity": "high", "issue": "Authenticator origin is not validated."})
    if not policy.get("rp_id_validation"):
        findings.append({"severity": "high", "issue": "Relying-party ID is not validated."})
    return findings
