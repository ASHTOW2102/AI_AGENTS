"""Flags API endpoints that enforce no maximum request body size, leaving them open to memory-exhaustion via oversized payloads."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("enforces_max_body_size"):
        findings.append({"severity": "high", "issue": "Endpoint enforces no maximum request body size."})
    return findings
