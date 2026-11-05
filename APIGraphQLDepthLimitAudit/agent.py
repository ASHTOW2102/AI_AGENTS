"""Checks GraphQL schemas for query-depth and field-count limits that prevent resource-exhaustion attacks."""
from typing import Any


def audit(schema: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not schema.get("max_query_depth_enforced"):
        findings.append({"severity": "high", "issue": "No maximum query depth is enforced."})
    if not schema.get("max_field_count_enforced"):
        findings.append({"severity": "medium", "issue": "No maximum field count per query is enforced."})
    if schema.get("has_circular_relationships") and schema.get("max_query_depth_enforced") is False:
        findings.append({"severity": "critical", "issue": "Circular relationships with no depth limit allow unbounded recursive queries."})
    return findings
