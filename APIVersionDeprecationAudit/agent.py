"""Flags API endpoints still serving a deprecated version with no sunset header or migration deadline communicated to clients, risking an abrupt breaking removal."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    is_deprecated = endpoint.get("is_deprecated_version", False)
    has_sunset_header = endpoint.get("sends_sunset_header", False)
    has_deadline = endpoint.get("sunset_date")

    if is_deprecated and not has_sunset_header:
        findings.append({"severity": "medium", "issue": "Endpoint serves a deprecated API version but does not send a Sunset header, giving clients no machine-readable migration signal."})
    if is_deprecated and not has_deadline:
        findings.append({"severity": "medium", "issue": "Deprecated endpoint has no communicated sunset date, risking an abrupt breaking removal for clients that haven't migrated."})
    return findings
