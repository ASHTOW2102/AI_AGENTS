"""Flags API endpoints that bind client-supplied JSON fields directly to internal model attributes without an allowlist, enabling mass assignment of protected fields."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    allowlist = endpoint.get("allowlisted_bindable_fields", [])
    protected = endpoint.get("protected_fields", [])

    if endpoint.get("binds_request_body_directly") and not allowlist:
        findings.append({"severity": "high", "issue": "Endpoint binds the request body directly with no allowlist, so every field including protected ones is bindable."})
    else:
        leaked = [f for f in protected if f in allowlist]
        if leaked:
            findings.append({"severity": "high", "issue": f"Protected fields are mistakenly allowlisted for client binding: {leaked}"})
    return findings
