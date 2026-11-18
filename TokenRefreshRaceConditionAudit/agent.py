"""Flags OAuth clients where concurrent requests can each trigger an independent token refresh, racing and invalidating each other's tokens."""
from typing import Any


def audit(client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if client.get("concurrent_requests_possible") and not client.get("refresh_request_deduplicated"):
        findings.append({"severity": "medium", "issue": "Concurrent requests can each trigger a separate token refresh, racing and invalidating tokens."})
    if not client.get("refresh_mutex_or_lock_used"):
        findings.append({"severity": "low", "issue": "No lock/mutex guards the token refresh operation."})
    return findings
