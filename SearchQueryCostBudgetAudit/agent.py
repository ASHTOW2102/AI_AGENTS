"""Flags search queries with no estimated-cost cutoff, letting a single pathological query consume disproportionate cluster resources."""
from typing import Any


def audit(query: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not query.get("cost_estimation_enabled"):
        findings.append({"severity": "high", "issue": "Query execution has no cost estimation to cut off expensive queries."})
    if query.get("cost_estimation_enabled") and query.get("estimated_cost", 0) > query.get("max_acceptable_cost", 1000) and not query.get("rejected"):
        findings.append({"severity": "medium", "issue": "Query exceeds the acceptable cost estimate but was not rejected."})
    return findings
