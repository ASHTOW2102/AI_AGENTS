"""Review cache-control policy for sensitive and versioned browser resources."""
from typing import Any


def audit(resource: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if resource.get("sensitive") and resource.get("shared_cache_allowed"):
        findings.append({"severity": "high", "issue": "Sensitive response may be stored in a shared cache."})
    if resource.get("sensitive") and resource.get("browser_cache_max_age", 0) > resource.get("max_sensitive_cache_age", 0):
        findings.append({"severity": "medium", "issue": "Sensitive browser cache lifetime exceeds policy."})
    if resource.get("immutable_asset") and not resource.get("content_hashed_url"):
        findings.append({"severity": "low", "issue": "Immutable asset URL is not content-versioned."})
    if resource.get("private_response") and not resource.get("vary_authorization"):
        findings.append({"severity": "high", "issue": "Personalized response cache does not vary on authorization."})
    return findings
