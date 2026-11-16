"""Flags database connection pools running near exhaustion with no queueing or backpressure for new requests."""
from typing import Any


def audit(pool: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    utilization = pool.get("active_connections", 0) / pool.get("max_connections", 1)
    if utilization > pool.get("max_acceptable_utilization", 0.85):
        findings.append({"severity": "high", "issue": "Connection pool utilization exceeds the acceptable threshold."})
    if not pool.get("queueing_enabled_on_exhaustion"):
        findings.append({"severity": "medium", "issue": "Pool has no request queueing configured for when it is exhausted."})
    return findings
