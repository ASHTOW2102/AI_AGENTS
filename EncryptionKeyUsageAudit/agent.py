"""Audit cryptographic key usage, purpose separation, and decommissioning."""
from typing import Any


def audit(key: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if len(set(key.get("purposes", []))) > 1 and not key.get("multi_purpose_approved"):
        findings.append({"severity": "high", "issue": "Key is reused across purposes without an approved exception."})
    if key.get("algorithm") not in set(key.get("approved_algorithms", [])):
        findings.append({"severity": "high", "issue": "Key algorithm is not on the approved list."})
    if key.get("decommissioned") and key.get("active_consumers", 0) > 0:
        findings.append({"severity": "critical", "issue": "Decommissioned key still has active consumers."})
    if key.get("exportable") and not key.get("export_exception_approved"):
        findings.append({"severity": "medium", "issue": "Key is exportable without an approved exception."})
    return findings
