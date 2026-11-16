"""Flags search query endpoints with no per-client rate limiting, risking expensive query abuse."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("rate_limit_configured"):
        findings.append({"severity": "high", "issue": "Search endpoint has no rate limiting configured."})
    if endpoint.get("supports_expensive_queries") and not endpoint.get("query_cost_estimation_enabled"):
        findings.append({"severity": "medium", "issue": "Endpoint supports expensive queries with no cost estimation to throttle them."})
    return findings
