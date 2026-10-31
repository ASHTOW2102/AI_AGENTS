"""Review SFTP endpoint authentication and host-key trust metadata."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("password_auth_enabled"):
        findings.append({"severity": "medium", "issue": "SFTP password authentication is enabled."})
    if not endpoint.get("host_key_pinned"):
        findings.append({"severity": "high", "issue": "SFTP server host key is not pinned or verified."})
    if endpoint.get("shared_private_key"):
        findings.append({"severity": "high", "issue": "SFTP private key is shared across identities."})
    if not endpoint.get("key_rotation_schedule"):
        findings.append({"severity": "low", "issue": "SFTP authentication key has no rotation schedule."})
    return findings
