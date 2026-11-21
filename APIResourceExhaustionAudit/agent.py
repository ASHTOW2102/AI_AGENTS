"""Flags API endpoints that accept unbounded array or nested-object input sizes, allowing a single request to exhaust server memory or CPU."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("accepts_array_input") and not endpoint.get("max_array_length_enforced"):
        findings.append({"severity": "high", "issue": "Endpoint accepts array input with no maximum length enforced."})
    if endpoint.get("accepts_nested_json") and not endpoint.get("max_nesting_depth_enforced"):
        findings.append({"severity": "medium", "issue": "Endpoint accepts nested JSON with no maximum nesting depth enforced."})
    return findings
