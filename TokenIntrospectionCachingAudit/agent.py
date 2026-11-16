"""Flags resource servers that cache token introspection results longer than the token's own expiry window."""
from typing import Any


def audit(resource_server: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if resource_server.get("introspection_cache_ttl_seconds", 0) > resource_server.get("token_ttl_seconds", 1):
        findings.append({"severity": "high", "issue": "Introspection cache TTL exceeds the token's own lifetime, risking use-after-revocation."})
    if not resource_server.get("cache_invalidated_on_revocation"):
        findings.append({"severity": "medium", "issue": "Introspection cache is not invalidated when a token is revoked."})
    return findings
