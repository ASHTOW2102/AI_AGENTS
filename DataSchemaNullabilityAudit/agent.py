"""Check dataset nullability changes against required-field contracts."""
from typing import Any


def audit(change: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    relaxed = sorted(set(change.get("required_non_null_fields", [])) & set(change.get("newly_nullable_fields", [])))
    if relaxed:
        findings.append({"severity": "high", "issue": "Required fields became nullable: " + ", ".join(relaxed)})
    if change.get("nullable_field_count", 0) > change.get("max_nullable_field_count", 0):
        findings.append({"severity": "medium", "issue": "Nullable field count exceeds the schema budget."})
    if change.get("null_rate_increase_percent", 0) > change.get("max_null_rate_increase_percent", 5):
        findings.append({"severity": "medium", "issue": "Observed null-rate increase exceeds policy."})
    return findings
