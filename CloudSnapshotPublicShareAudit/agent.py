"""Flags disk/database snapshots shared publicly, at high severity when the snapshot is also known to contain sensitive data."""
from typing import Any


def audit(snapshot: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if snapshot.get("publicly_shared"):
        severity = "high" if snapshot.get("contains_sensitive_data") else "medium"
        findings.append({"severity": severity, "issue": "Snapshot is shared publicly."})
    return findings
