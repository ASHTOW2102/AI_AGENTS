"""Checks feature-store access grants for sensitive features against approved consumer lists."""
from typing import Any


def audit(feature: dict[str, Any]):
    findings = []
    unapproved = sorted(set(feature.get("consumers", [])) - set(feature.get("approved_consumers", [])))
    if unapproved:
        findings.append({"severity": "high", "issue": "Unapproved consumers access this feature: " + ", ".join(unapproved)})
    if feature.get("sensitive") and not feature.get("access_logged"):
        findings.append({"severity": "high", "issue": "Sensitive feature access is not logged."})
    if feature.get("sensitive") and feature.get("row_level_filtering_required") and not feature.get("row_level_filtering_enabled"):
        findings.append({"severity": "medium", "issue": "Required row-level filtering is not enabled."})
    return findings
