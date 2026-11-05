"""Checks rate-limited API responses for standard throttle headers clients can act on."""
from typing import Any


def audit(response: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    headers = response.get("headers", {})
    if response.get("status") == 429 and "Retry-After" not in headers:
        findings.append({"severity": "medium", "issue": "429 response has no Retry-After header."})
    if response.get("rate_limited_endpoint") and "X-RateLimit-Remaining" not in headers:
        findings.append({"severity": "low", "issue": "Rate-limited endpoint does not expose remaining-quota headers."})
    if response.get("status") == 429 and response.get("body_cacheable"):
        findings.append({"severity": "medium", "issue": "429 response is marked cacheable, risking stale throttle state."})
    return findings
