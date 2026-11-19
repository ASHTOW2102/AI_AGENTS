"""Flags API endpoints that silently fall back to a default response format when the Accept header is unrecognized, instead of returning 406."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("unrecognized_accept_falls_back_silently") and not endpoint.get("fallback_documented"):
        findings.append({"severity": "low", "issue": "Unrecognized Accept header silently falls back to a default format instead of returning 406."})
    if endpoint.get("supports_multiple_formats") and not endpoint.get("vary_header_includes_accept"):
        findings.append({"severity": "medium", "issue": "Endpoint supports multiple formats but Vary header does not include Accept, risking cache poisoning across formats."})
    return findings
