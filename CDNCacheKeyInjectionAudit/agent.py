"""Flags CDN configurations that include unvalidated headers or query parameters in the cache key, allowing an attacker to poison the shared cache with a malicious response for other users."""
from typing import Any


def audit(cdn_config: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    unvalidated_header_in_key = cdn_config.get("includes_unvalidated_header_in_cache_key", False)
    unbounded_query_params = cdn_config.get("includes_all_query_params_in_cache_key", False)

    if unvalidated_header_in_key:
        findings.append({"severity": "high", "issue": "An unvalidated request header is part of the cache key, allowing cache-poisoning by crafting a header value that causes a malicious cached response to be served to other users."})
    if unbounded_query_params:
        findings.append({"severity": "medium", "issue": "All query parameters are included in the cache key without an allowlist, letting an attacker fragment the cache with junk parameters to cause excessive cache misses or poisoning."})
    return findings
