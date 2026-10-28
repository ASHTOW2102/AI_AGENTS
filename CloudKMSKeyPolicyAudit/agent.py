"""Review managed-key policy metadata for rotation and administrative separation."""
from typing import Any


def audit(key: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not key.get("rotation_enabled"):
        findings.append({"severity": "medium", "issue": "Managed-key rotation is not enabled."})
    if key.get("key_admins_overlap_data_readers"):
        findings.append({"severity": "high", "issue": "Key administrators also have access to protected data."})
    if key.get("decrypt_permission_principal_count", 0) > key.get("max_decrypt_principals", 0):
        findings.append({"severity": "medium", "issue": "Decrypt permission is granted to too many principals."})
    if key.get("disabled") and key.get("active_dependents", 0) > 0:
        findings.append({"severity": "high", "issue": "Disabled key still has active dependent workloads."})
    return findings
