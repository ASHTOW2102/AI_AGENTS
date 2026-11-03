"""Checks API field-mask/partial-response support for over-fetching of sensitive fields."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("supports_field_mask") and endpoint.get("sensitive_fields_excluded_by_default") is False:
        findings.append({"severity": "high", "issue": "Sensitive fields are returned by default when a field mask is not supplied."})
    if not endpoint.get("supports_field_mask") and endpoint.get("response_contains_sensitive_fields"):
        findings.append({"severity": "medium", "issue": "Endpoint has no field mask and always returns sensitive fields."})
    if endpoint.get("field_mask_injection_possible"):
        findings.append({"severity": "high", "issue": "Field mask parameter is not validated against an allowlist of fields."})
    return findings
