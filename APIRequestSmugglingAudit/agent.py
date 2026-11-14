"""Flags API endpoints vulnerable to request smuggling via inconsistent Content-Length/Transfer-Encoding handling."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("supports_chunked_encoding") and endpoint.get("front_end_and_back_end_parsers_differ"):
        findings.append({"severity": "high", "issue": "Front-end and back-end parsers disagree on chunked encoding, risking request smuggling."})
    if not endpoint.get("strict_content_length_validation"):
        findings.append({"severity": "medium", "issue": "No strict Content-Length validation is enforced."})
    return findings
