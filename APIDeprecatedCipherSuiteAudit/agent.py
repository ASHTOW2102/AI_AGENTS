"""Flags API endpoints that still negotiate deprecated or weak TLS cipher suites."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    weak = {"RC4", "3DES", "NULL", "EXPORT"}
    offered_weak = [c for c in endpoint.get("offered_ciphers", []) if any(w in c for w in weak)]
    if offered_weak:
        findings.append({"severity": "high", "issue": f"Endpoint offers weak cipher suites: {offered_weak}"})
    if not endpoint.get("forward_secrecy_enforced"):
        findings.append({"severity": "medium", "issue": "Endpoint does not enforce forward-secret cipher suites."})
    return findings
