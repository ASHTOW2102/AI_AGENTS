"""Review API write endpoints for explicit idempotency contracts."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("retryable_write") and not endpoint.get("idempotency_key_supported"):
        findings.append({"severity": "high", "issue": "Retryable write endpoint has no idempotency-key support."})
    if endpoint.get("idempotency_key_supported") and endpoint.get("key_retention_hours", 0) < endpoint.get("max_retry_window_hours", 0):
        findings.append({"severity": "medium", "issue": "Idempotency record expires before the retry window."})
    if endpoint.get("key_supported") and not endpoint.get("payload_conflict_rejected"):
        findings.append({"severity": "medium", "issue": "Reusing a key with a different payload is not rejected."})
    return findings
