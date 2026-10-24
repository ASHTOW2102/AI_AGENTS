"""Evaluate cache stampede protection and stale-data fallback metadata."""
from typing import Any


def audit(cache: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if cache.get("ttl_seconds", 0) <= 0:
        findings.append({"severity": "medium", "issue": "Cache entries have no positive TTL."})
    if not cache.get("request_coalescing") and not cache.get("refresh_lock"):
        findings.append({"severity": "high", "issue": "Concurrent cache misses can trigger duplicate origin work."})
    if cache.get("refresh_jitter_percent", 0) <= 0:
        findings.append({"severity": "medium", "issue": "Refresh schedule has no TTL jitter."})
    if cache.get("stale_fallback_expected") and not cache.get("stale_fallback_enabled"):
        findings.append({"severity": "medium", "issue": "Stale-if-error fallback is expected but not enabled."})
    return findings
