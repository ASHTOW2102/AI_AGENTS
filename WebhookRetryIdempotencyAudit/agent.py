"""Flags webhook receivers that support provider-side retry delivery but do not check an idempotency key, risking duplicate processing of the same event."""
from typing import Any


def audit(webhook_endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if webhook_endpoint.get("supports_retries") and not webhook_endpoint.get("has_idempotency_key_check"):
        findings.append({"severity": "high", "issue": "Webhook endpoint accepts retried deliveries without an idempotency key check, risking duplicate processing."})
    return findings
