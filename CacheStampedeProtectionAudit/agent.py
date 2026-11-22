"""Flags caching layers with no stampede protection (lock, early recomputation, or request coalescing), where a cache-key expiry under high concurrency causes a thundering herd of simultaneous origin requests."""
from typing import Any


def audit(cache: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    has_lock = cache.get("uses_recompute_lock", False)
    has_early_refresh = cache.get("uses_early_expiry_jitter", False)
    high_concurrency = cache.get("expected_concurrent_requests", 0) > 50

    if high_concurrency and not has_lock and not has_early_refresh:
        findings.append({"severity": "high", "issue": "High-concurrency cache key has no stampede protection (recompute lock or jittered early expiry), risking a thundering herd on expiry."})
    if cache.get("ttl_seconds", 0) == 0 and not cache.get("negative_cache_ttl"):
        findings.append({"severity": "medium", "issue": "Cache has no TTL and no negative-cache policy, which can mask stampede risk analysis."})
    return findings
