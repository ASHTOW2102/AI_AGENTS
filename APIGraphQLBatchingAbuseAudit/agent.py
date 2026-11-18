"""Flags GraphQL endpoints that allow unbounded query batching, letting a single HTTP request bypass per-request rate limits."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("max_batch_size"):
        findings.append({"severity": "high", "issue": "GraphQL endpoint has no limit on batched queries per request."})
    if endpoint.get("rate_limit_applies_per") == "http_request" and endpoint.get("max_batch_size", 0) > 1:
        findings.append({"severity": "medium", "issue": "Rate limiting is applied per HTTP request, so batching multiple queries bypasses it."})
    return findings
