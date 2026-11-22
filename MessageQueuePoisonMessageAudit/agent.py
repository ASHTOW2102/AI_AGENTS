"""Flags message queue consumers with no dead-letter queue or max-retry limit, where a single malformed 'poison' message is redelivered indefinitely and blocks the queue."""
from typing import Any


def audit(consumer: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    has_dlq = consumer.get("has_dead_letter_queue", False)
    max_retries = consumer.get("max_delivery_attempts")

    if not max_retries:
        findings.append({"severity": "high", "issue": "Consumer has no maximum delivery attempt limit, so a malformed message can be redelivered indefinitely and block the queue."})
    if not has_dlq:
        findings.append({"severity": "high", "issue": "Consumer has no dead-letter queue configured, so poison messages that exhaust retries are lost rather than retained for inspection."})
    return findings
