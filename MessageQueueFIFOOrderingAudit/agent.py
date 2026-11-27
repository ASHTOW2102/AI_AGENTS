"""Flags workloads that require strict message ordering but run on a standard (non-FIFO) queue, which offers no ordering guarantee."""
from typing import Any


def audit(queue: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if queue.get("requires_strict_ordering") and queue.get("queue_type") != "fifo":
        findings.append({"severity": "high", "issue": f"Ordering-dependent workload runs on a '{queue.get('queue_type')}' queue with no ordering guarantee."})
    return findings
