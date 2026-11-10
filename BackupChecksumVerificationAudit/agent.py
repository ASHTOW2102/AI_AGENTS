"""Checks that backup artifacts have post-write checksum verification to catch silent corruption."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not backup.get("checksum_verified_after_write"):
        findings.append({"severity": "high", "issue": "Backup has no checksum verification after write."})
    if backup.get("checksum_verified_after_write") and backup.get("checksum_mismatch_count", 0) > 0:
        findings.append({"severity": "high", "issue": "Backup checksum mismatches were detected and not resolved."})
    return findings
