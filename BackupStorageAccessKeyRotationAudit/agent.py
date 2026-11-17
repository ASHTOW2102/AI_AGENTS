"""Flags static access keys used to write backups to storage that have not been rotated within policy."""
from typing import Any


def audit(credential: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if credential.get("key_age_days", 0) > credential.get("max_acceptable_age_days", 90):
        findings.append({"severity": "high", "issue": "Backup storage access key exceeds the maximum rotation age."})
    if credential.get("key_type") == "static" and not credential.get("rotation_automated"):
        findings.append({"severity": "medium", "issue": "Static backup access key has no automated rotation process."})
    return findings
