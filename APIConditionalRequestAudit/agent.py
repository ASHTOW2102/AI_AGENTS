"""Flags API endpoints that don't support conditional requests (If-Match/If-None-Match), allowing lost-update race conditions on concurrent writes."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("supports_concurrent_writes") and not endpoint.get("supports_etag_conditional_requests"):
        findings.append({"severity": "high", "issue": "Endpoint allows concurrent writes with no ETag-based conditional request support."})
    if endpoint.get("supports_etag_conditional_requests") and not endpoint.get("returns_412_on_mismatch"):
        findings.append({"severity": "medium", "issue": "Conditional requests are supported but mismatches do not return 412 Precondition Failed."})
    return findings
