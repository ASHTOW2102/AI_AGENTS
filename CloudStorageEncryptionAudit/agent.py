"""Review cloud storage encryption defaults and key ownership metadata."""
from typing import Any


def audit(storage: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not storage.get("encryption_at_rest_enabled"):
        findings.append({"severity": "critical", "issue": "Storage encryption at rest is disabled."})
    if storage.get("customer_managed_key_required") and not storage.get("customer_managed_key_configured"):
        findings.append({"severity": "high", "issue": "Required customer-managed key is not configured."})
    if storage.get("key_rotation_days", 0) > storage.get("max_key_rotation_days", 365):
        findings.append({"severity": "medium", "issue": "Encryption key rotation interval exceeds policy."})
    if storage.get("unencrypted_object_count", 0) > 0:
        findings.append({"severity": "high", "issue": "Storage inventory contains unencrypted objects."})
    return findings
