"""Review event schema changes for consumer-safe evolution."""
from typing import Any


def audit(change: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if change.get("required_field_added"):
        findings.append({"severity": "high", "issue": "New required event field may break existing producers."})
    if change.get("field_type_changed"):
        findings.append({"severity": "high", "issue": "Existing event field type changed incompatibly."})
    if change.get("enum_value_removed"):
        findings.append({"severity": "medium", "issue": "Event enum value was removed while consumers may still emit it."})
    if change.get("breaking_change") and not change.get("schema_version_incremented"):
        findings.append({"severity": "medium", "issue": "Breaking event schema change has no version increment."})
    return findings
