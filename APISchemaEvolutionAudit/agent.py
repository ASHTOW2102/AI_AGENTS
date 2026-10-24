"""Review API schema changes for breaking evolution hazards."""
from typing import Any


def audit(change: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if change.get("removed_fields"):
        findings.append({"severity": "high", "issue": "Schema removes fields: " + ", ".join(sorted(change["removed_fields"]))})
    if change.get("required_fields_added"):
        findings.append({"severity": "high", "issue": "Schema adds required fields that can break existing clients."})
    if change.get("enum_values_removed"):
        findings.append({"severity": "medium", "issue": "Schema removes enum values used by existing clients."})
    if change.get("breaking_change") and not change.get("major_version_bumped"):
        findings.append({"severity": "medium", "issue": "Breaking schema change has no major version increment."})
    return findings
