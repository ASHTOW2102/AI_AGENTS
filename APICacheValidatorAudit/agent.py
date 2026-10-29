"""Review API caching policy for validators and safe revalidation."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("cacheable") and not endpoint.get("etag_or_last_modified"):
        findings.append({"severity": "low", "issue": "Cacheable response has no conditional request validator."})
    if endpoint.get("personalized") and endpoint.get("shared_cache_enabled"):
        findings.append({"severity": "high", "issue": "Personalized response is eligible for shared caching."})
    if endpoint.get("sensitive") and endpoint.get("cache_max_age_seconds", 0) > 0:
        findings.append({"severity": "medium", "issue": "Sensitive response is configured for positive cache retention."})
    if endpoint.get("stale_while_revalidate_seconds", 0) > endpoint.get("max_stale_seconds", 0):
        findings.append({"severity": "medium", "issue": "Stale-while-revalidate duration exceeds policy."})
    return findings
