"""Flags proxy chains where the frontend and backend disagree on strict chunked-encoding parsing, a classic request-smuggling/desync precondition."""
from typing import Any


def audit(proxy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    frontend_strict = proxy.get("frontend_parses_chunked_strictly")
    backend_strict = proxy.get("backend_parses_chunked_strictly")
    if frontend_strict != backend_strict:
        findings.append({"severity": "high", "issue": "Frontend and backend disagree on strict chunked-encoding parsing, enabling request desync."})
    return findings
