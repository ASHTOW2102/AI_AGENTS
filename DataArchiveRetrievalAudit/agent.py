"""Check archive retrieval readiness, ownership, and restore timing."""
from typing import Any


def audit(archive: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not archive.get("retrieval_procedure"):
        findings.append({"severity": "medium", "issue": "Archive has no documented retrieval procedure."})
    if archive.get("measured_retrieval_hours", 0) > archive.get("target_retrieval_hours", 0):
        findings.append({"severity": "high", "issue": "Measured retrieval time exceeds the target."})
    if not archive.get("restore_permission_tested"):
        findings.append({"severity": "medium", "issue": "Archive restore permissions have not been tested."})
    if not archive.get("owner"):
        findings.append({"severity": "low", "issue": "No owner is assigned to the archive."})
    return findings
