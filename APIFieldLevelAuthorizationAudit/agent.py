"""Flags API endpoints that enforce authorization at the object level but not at the individual field level."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    sensitive_exposed = [f for f in endpoint.get("sensitive_fields", []) if f not in endpoint.get("field_level_authorized_fields", [])]
    if sensitive_exposed:
        findings.append({"severity": "high", "issue": f"Sensitive fields are returned without field-level authorization: {sensitive_exposed}"})
    if endpoint.get("object_level_authorized") and not endpoint.get("field_level_authorization_enabled"):
        findings.append({"severity": "medium", "issue": "Object-level authorization exists but no field-level checks are performed."})
    return findings
