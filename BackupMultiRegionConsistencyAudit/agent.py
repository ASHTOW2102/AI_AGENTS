"""Flags multi-region backup copies that have diverged from the primary copy's checksum, indicating a silent replication failure."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if backup.get("primary_checksum") != backup.get("replica_checksum"):
        findings.append({"severity": "high", "issue": "Replica backup checksum does not match the primary, indicating silent replication corruption or drift."})
    if not backup.get("checksum_comparison_automated"):
        findings.append({"severity": "medium", "issue": "Checksum comparison between regions is not automated."})
    return findings
