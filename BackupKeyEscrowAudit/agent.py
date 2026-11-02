"""Checks backup-encryption key escrow for recovery access and single-person-control risk."""
from typing import Any


def audit(key: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not key.get("escrowed"):
        findings.append({"severity": "critical", "issue": "Backup encryption key is not escrowed anywhere recoverable."})
    if key.get("escrowed") and key.get("escrow_holder_count", 0) < 2:
        findings.append({"severity": "high", "issue": "Only one person can access the escrowed key."})
    if key.get("escrow_access_logged") is False:
        findings.append({"severity": "medium", "issue": "Escrow key access is not logged."})
    return findings
