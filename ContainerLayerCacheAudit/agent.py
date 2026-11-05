"""Checks container build layer ordering for cache-busting inefficiency and secret leakage into layers."""
from typing import Any


def audit(build: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if build.get("dependency_install_after_source_copy"):
        findings.append({"severity": "medium", "issue": "Dependency installation happens after source copy, busting the cache on every change."})
    if build.get("secret_used_in_build") and not build.get("secret_mount_type_used"):
        findings.append({"severity": "critical", "issue": "A build secret is baked into an image layer instead of using a secret mount."})
    if build.get("cache_hit_rate_percent", 100) < build.get("expected_cache_hit_rate_percent", 50):
        findings.append({"severity": "low", "issue": "Build cache hit rate is lower than expected."})
    return findings
