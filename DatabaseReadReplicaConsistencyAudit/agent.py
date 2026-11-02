"""Checks read-replica staleness against consistency requirements for read-after-write paths."""
from typing import Any


def audit(replica: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if replica.get("lag_ms", 0) > replica.get("max_tolerable_lag_ms", 1000):
        findings.append({"severity": "high", "issue": "Replica lag exceeds the tolerable staleness bound."})
    if replica.get("read_after_write_required") and not replica.get("sticky_routing_or_primary_read"):
        findings.append({"severity": "high", "issue": "Read-after-write path has no routing safeguard against stale replicas."})
    if replica.get("lag_monitoring_enabled") is False:
        findings.append({"severity": "medium", "issue": "Replica lag has no monitoring configured."})
    return findings
