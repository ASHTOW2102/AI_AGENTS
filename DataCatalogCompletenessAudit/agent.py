"""Checks data-catalog entries for description, ownership, and classification completeness."""
from typing import Any


def audit(entry: dict[str, Any]):
    findings = []
    if not entry.get("description"):
        findings.append({"severity": "medium", "issue": "Catalog entry has no description."})
    if not entry.get("owner"):
        findings.append({"severity": "high", "issue": "Catalog entry has no owner."})
    if not entry.get("classification"):
        findings.append({"severity": "high", "issue": "Catalog entry has no data classification."})
    if entry.get("classification") == "restricted" and not entry.get("access_control_documented"):
        findings.append({"severity": "high", "issue": "Restricted data has no documented access control."})
    return findings
