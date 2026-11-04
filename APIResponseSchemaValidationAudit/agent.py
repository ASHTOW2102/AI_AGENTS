"""Checks API responses are validated against a declared schema before being sent to clients."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("response_schema_declared"):
        findings.append({"severity": "medium", "issue": "Endpoint has no declared response schema."})
    if endpoint.get("response_schema_declared") and not endpoint.get("schema_validated_before_send"):
        findings.append({"severity": "high", "issue": "Declared response schema is not validated before sending."})
    if endpoint.get("schema_validation_failures_in_production", 0) > 0 and not endpoint.get("validation_failure_alerting"):
        findings.append({"severity": "medium", "issue": "Schema validation failures occur without alerting."})
    return findings
