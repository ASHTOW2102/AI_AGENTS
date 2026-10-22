"""Check database replica freshness and failover eligibility metrics."""
from typing import Any


def audit(replica: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if replica.get("lag_seconds", 0) > replica.get("max_lag_seconds", 0):
        findings.append({"severity": "high", "issue": "Replica lag exceeds the configured maximum."})
    if not replica.get("replication_healthy"):
        findings.append({"severity": "high", "issue": "Replication health is not confirmed."})
    if replica.get("failover_eligible") and not replica.get("promotion_tested"):
        findings.append({"severity": "medium", "issue": "Replica is marked failover-eligible without a promotion test."})
    if replica.get("replay_queue_bytes", 0) > replica.get("max_replay_queue_bytes", 0):
        findings.append({"severity": "medium", "issue": "Replica replay queue exceeds its capacity threshold."})
    return findings
