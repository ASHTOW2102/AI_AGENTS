"""Checks outbound webhook delivery rate limits and receiver backoff handling."""
from typing import Any


def audit(webhook: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not webhook.get("rate_limit_configured"):
        findings.append({"severity": "medium", "issue": "Outbound webhook delivery has no rate limit configured."})
    if webhook.get("receiver_429_count", 0) > 0 and not webhook.get("backoff_on_429"):
        findings.append({"severity": "high", "issue": "Receiver throttling responses do not trigger backoff."})
    if webhook.get("concurrent_deliveries", 0) > webhook.get("max_concurrent_deliveries", 0):
        findings.append({"severity": "medium", "issue": "Concurrent delivery count exceeds the configured maximum."})
    return findings
