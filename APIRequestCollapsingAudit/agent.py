"""Flags expensive API endpoints with no request collapsing, letting a thundering herd of identical concurrent requests all hit the backend."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("is_expensive_operation") and not endpoint.get("request_collapsing_enabled"):
        findings.append({"severity": "medium", "issue": "Expensive endpoint has no request collapsing for duplicate concurrent requests."})
    if endpoint.get("request_collapsing_enabled") and not endpoint.get("collapsing_key_includes_auth_scope"):
        findings.append({"severity": "high", "issue": "Request collapsing key does not include authorization scope, risking cross-user response sharing."})
    return findings
