"""Review SSH key inventory for age, ownership, and revocation hygiene."""
from typing import Any


def audit(key: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if key.get("age_days", 0) > key.get("max_age_days", 365):
        findings.append({"severity": "medium", "issue": "SSH key exceeds its maximum age."})
    if not key.get("owner"):
        findings.append({"severity": "medium", "issue": "SSH key has no recorded owner."})
    if key.get("owner_active") is False and not key.get("revoked"):
        findings.append({"severity": "high", "issue": "Key belonging to an inactive owner remains valid."})
    if key.get("privileged") and not key.get("hardware_backed"):
        findings.append({"severity": "high", "issue": "Privileged SSH key is not hardware-backed."})
    return findings
