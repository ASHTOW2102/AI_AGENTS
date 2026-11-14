"""Flags cloud disk snapshots that are not encrypted or use a non-rotated encryption key."""
from typing import Any


def audit(snapshot: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not snapshot.get("encrypted"):
        findings.append({"severity": "high", "issue": "Disk snapshot is not encrypted."})
    if snapshot.get("encrypted") and snapshot.get("key_age_days", 0) > snapshot.get("max_acceptable_key_age_days", 365):
        findings.append({"severity": "medium", "issue": "Snapshot encryption key exceeds the acceptable rotation age."})
    return findings
