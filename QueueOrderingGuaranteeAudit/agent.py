"""Review queue partitioning and processing configuration for ordering guarantees."""
from typing import Any


def audit(queue: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if queue.get("ordering_required") and queue.get("partition_key") is None:
        findings.append({"severity": "high", "issue": "Ordered processing is required but no partition key is defined."})
    if queue.get("ordering_required") and queue.get("consumer_parallelism", 1) > 1 and not queue.get("per_key_serialization"):
        findings.append({"severity": "high", "issue": "Parallel consumers do not preserve per-key message order."})
    if queue.get("retry_can_reorder") and not queue.get("retry_ordering_policy"):
        findings.append({"severity": "medium", "issue": "Retry behavior can reorder events without a documented policy."})
    if queue.get("dead_letter_requeue_enabled") and not queue.get("requeue_sequence_handled"):
        findings.append({"severity": "low", "issue": "Dead-letter requeue ordering behavior is undefined."})
    return findings
