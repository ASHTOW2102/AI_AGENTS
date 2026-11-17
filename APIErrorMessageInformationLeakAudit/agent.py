"""Flags API endpoints that return raw stack traces or internal exception messages to clients in error responses."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("returns_stack_trace_to_client"):
        findings.append({"severity": "high", "issue": "Error response includes a raw stack trace visible to the client."})
    if endpoint.get("error_message_includes_internal_paths"):
        findings.append({"severity": "medium", "issue": "Error message exposes internal file paths or hostnames."})
    return findings
