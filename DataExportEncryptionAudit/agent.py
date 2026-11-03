"""Checks data-export files for encryption at rest and secure transfer to recipients."""
from typing import Any


def audit(export: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if export.get("contains_sensitive_data") and not export.get("file_encrypted"):
        findings.append({"severity": "high", "issue": "Sensitive data export is not encrypted."})
    if export.get("file_encrypted") and not export.get("key_shared_via_secure_channel"):
        findings.append({"severity": "high", "issue": "Encryption key is not shared through a secure out-of-band channel."})
    if export.get("transfer_protocol") in (None, "ftp", "http"):
        findings.append({"severity": "medium", "issue": "Export is transferred over an insecure protocol."})
    return findings
