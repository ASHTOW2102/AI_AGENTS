"""Flags API endpoints that pass a client-supplied sort parameter directly into a database ORDER BY clause."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("sort_param_from_client") and not endpoint.get("sort_param_allowlisted"):
        findings.append({"severity": "high", "issue": "Client-supplied sort parameter is not validated against an allowlist of columns."})
    if endpoint.get("sort_param_from_client") and endpoint.get("sort_param_concatenated_into_sql"):
        findings.append({"severity": "high", "issue": "Sort parameter is concatenated directly into SQL."})
    return findings
