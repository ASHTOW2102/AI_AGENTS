"""Audits CDN cache invalidation coverage and propagation delay for published content changes."""
from typing import Any


def audit(cdn: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if cdn.get("content_changed") and not cdn.get("invalidation_triggered"):
        findings.append({"severity": "high", "issue": "Content changed but no cache invalidation was triggered."})
    if cdn.get("invalidation_propagation_ms", 0) > cdn.get("max_acceptable_propagation_ms", 60000):
        findings.append({"severity": "medium", "issue": "Cache invalidation propagation exceeds the acceptable delay."})
    if not cdn.get("stale_while_revalidate_configured"):
        findings.append({"severity": "low", "issue": "No stale-while-revalidate policy configured for cache misses."})
    return findings
