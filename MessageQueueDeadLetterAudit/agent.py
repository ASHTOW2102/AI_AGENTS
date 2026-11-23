"""Flags message queues with no dead-letter queue configured, so poison messages are retried forever or silently dropped instead of being surfaced."""
from typing import Any


def audit(queue: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not queue.get("dead_letter_queue_configured"):
        findings.append({"severity": "high", "issue": "Queue has no dead-letter queue configured; poison messages are retried indefinitely or dropped silently."})
    return findings
