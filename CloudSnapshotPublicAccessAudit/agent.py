"""Review cloud snapshot access, sharing, and public-exposure metadata."""
from typing import Any


def audit(snapshot: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if snapshot.get("publicly_shared"):
        findings.append({"severity": "critical", "issue": "Snapshot is shared publicly."})
    if snapshot.get("cross_account_shared") and not snapshot.get("sharing_approved"):
        findings.append({"severity": "high", "issue": "Snapshot is shared across accounts without approval."})
    if snapshot.get("sensitive_data") and not snapshot.get("encryption_confirmed"):
        findings.append({"severity": "high", "issue": "Sensitive snapshot encryption is not confirmed."})
    if snapshot.get("obsolete_days", 0) > snapshot.get("max_obsolete_days", 90) and not snapshot.get("retention_exception"):
        findings.append({"severity": "low", "issue": "Snapshot exceeds the allowed age without a retention exception."})
    return findings
