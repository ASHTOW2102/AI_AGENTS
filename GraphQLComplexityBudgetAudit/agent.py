"""Check GraphQL query complexity limits and depth protections."""
from typing import Any


def audit(schema: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not schema.get("complexity_limit_enabled"):
        findings.append({"severity": "high", "issue": "GraphQL query complexity is not bounded."})
    if schema.get("max_query_depth", 0) > schema.get("approved_max_depth", 10):
        findings.append({"severity": "medium", "issue": "Maximum query depth exceeds the approved limit."})
    if schema.get("list_fields_without_pagination", 0) > 0:
        findings.append({"severity": "medium", "issue": "List fields allow unbounded result sets."})
    if schema.get("batching_enabled") and not schema.get("batch_size_limit"):
        findings.append({"severity": "high", "issue": "Query batching has no batch-size limit."})
    return findings
