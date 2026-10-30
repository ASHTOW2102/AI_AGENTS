"""Review build-cache trust boundaries and integrity verification metadata."""
from typing import Any


def audit(cache: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if cache.get("shared_between_trust_levels") and not cache.get("cache_namespace_isolated"):
        findings.append({"severity": "high", "issue": "Build cache is shared across trust levels without isolation."})
    if cache.get("remote_cache_enabled") and not cache.get("artifact_integrity_verified"):
        findings.append({"severity": "high", "issue": "Remote build-cache artifacts are not integrity verified."})
    if cache.get("untrusted_pull_requests_write_cache"):
        findings.append({"severity": "critical", "issue": "Untrusted pull requests can write to a trusted build cache."})
    if not cache.get("cache_retention_bounded"):
        findings.append({"severity": "low", "issue": "Build-cache retention is not bounded."})
    return findings
