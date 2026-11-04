"""Checks internal DNS resolver redundancy and failover behavior under resolver outages."""
from typing import Any


def audit(resolver: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if resolver.get("resolver_count", 0) < 2:
        findings.append({"severity": "high", "issue": "Only a single DNS resolver is configured with no failover."})
    if resolver.get("resolver_count", 0) >= 2 and not resolver.get("failover_tested"):
        findings.append({"severity": "medium", "issue": "Multiple resolvers are configured but failover has not been tested."})
    if resolver.get("negative_cache_ttl_seconds", 0) > resolver.get("max_acceptable_negative_ttl_seconds", 300):
        findings.append({"severity": "low", "issue": "Negative-response caching is longer than recommended."})
    return findings
