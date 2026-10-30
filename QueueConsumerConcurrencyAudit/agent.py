"""Review queue consumer concurrency and partition-consumption limits."""
from typing import Any


def audit(consumer: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if consumer.get("workers", 0) > consumer.get("partitions", 0) and consumer.get("one_worker_per_partition"):
        findings.append({"severity": "low", "issue": "Consumer worker count exceeds available partitions."})
    if consumer.get("max_inflight_messages", 0) > consumer.get("approved_max_inflight", 0):
        findings.append({"severity": "medium", "issue": "In-flight message count exceeds the approved limit."})
    if consumer.get("concurrency_enabled") and not consumer.get("downstream_capacity_budgeted"):
        findings.append({"severity": "high", "issue": "Parallel consumption is not bounded by downstream capacity."})
    if consumer.get("ordering_required") and consumer.get("parallelism", 1) > 1 and not consumer.get("key_ordering_preserved"):
        findings.append({"severity": "high", "issue": "Parallel processing can violate required message ordering."})
    return findings
