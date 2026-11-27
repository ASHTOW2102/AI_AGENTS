"""Flags API endpoints that expose raw stack traces in error responses, leaking internal file paths, library versions, and logic to any client."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("exposes_stack_traces_in_errors"):
        findings.append({"severity": "high", "issue": "Endpoint exposes raw stack traces in error responses."})
    return findings
