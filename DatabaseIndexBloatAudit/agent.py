"""Flags database indexes with excessive bloat ratio that degrade query performance."""
from typing import Any


def audit(index: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if index.get("bloat_ratio", 0) > index.get("max_acceptable_bloat_ratio", 0.3):
        findings.append({"severity": "medium", "issue": "Index bloat ratio exceeds the acceptable threshold."})
    if not index.get("reindex_scheduled") and index.get("bloat_ratio", 0) > 0.5:
        findings.append({"severity": "high", "issue": "Severely bloated index has no scheduled reindex."})
    if index.get("unused_for_days", 0) > 90:
        findings.append({"severity": "low", "issue": "Index has not been used in over 90 days."})
    return findings
