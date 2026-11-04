"""Checks backup artifacts for post-write checksum verification against source data."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not backup.get("checksum_computed_at_write_time"):
        findings.append({"severity": "high", "issue": "Backup has no checksum computed at write time."})
    if backup.get("checksum_computed_at_write_time") and not backup.get("checksum_verified_on_restore_test"):
        findings.append({"severity": "medium", "issue": "Checksum is never verified during restore testing."})
    if backup.get("checksum_mismatch_detected") and not backup.get("mismatch_alerting_enabled"):
        findings.append({"severity": "high", "issue": "Checksum mismatches are detected but do not trigger alerts."})
    return findings
