"""Flags deprecated API endpoints that do not advertise a Sunset header, leaving client developers with no machine-readable deprecation timeline."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("is_deprecated") and not endpoint.get("has_sunset_header"):
        findings.append({"severity": "low", "issue": "Deprecated endpoint does not advertise a Sunset header."})
    return findings
