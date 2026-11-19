"""Flags search result caches with a TTL longer than the underlying index's update frequency, serving outdated results as if current."""
from typing import Any


def audit(cache: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if cache.get("ttl_seconds", 0) > cache.get("index_update_interval_seconds", 1):
        findings.append({"severity": "medium", "issue": "Cache TTL exceeds the index update interval, risking stale results."})
    if not cache.get("cache_invalidated_on_index_update"):
        findings.append({"severity": "low", "issue": "Cache is not proactively invalidated when the index updates."})
    return findings
