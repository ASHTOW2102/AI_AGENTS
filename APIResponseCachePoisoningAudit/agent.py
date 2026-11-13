"""Flags API endpoints at risk of cache poisoning from unkeyed request inputs reflected into cached responses."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    unkeyed = set(endpoint.get("response_varying_headers", [])) - set(endpoint.get("cache_key_headers", []))
    if unkeyed:
        findings.append({"severity": "high", "issue": f"Response varies on headers not in the cache key: {sorted(unkeyed)}"})
    if endpoint.get("cached") and not endpoint.get("cache_key_includes_auth_scope"):
        findings.append({"severity": "high", "issue": "Cached response does not key on authorization scope."})
    return findings
