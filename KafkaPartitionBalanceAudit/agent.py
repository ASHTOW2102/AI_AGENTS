"""Review partition distribution and leader skew across broker nodes."""
from typing import Any


def audit(cluster: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    counts = cluster.get("partitions_per_broker", [])
    if counts and max(counts) - min(counts) > cluster.get("max_partition_spread", 10):
        findings.append({"severity": "medium", "issue": "Partition counts are uneven across brokers."})
    leaders = cluster.get("leaders_per_broker", [])
    if leaders and max(leaders) - min(leaders) > cluster.get("max_leader_spread", 10):
        findings.append({"severity": "medium", "issue": "Partition leadership is uneven across brokers."})
    if cluster.get("under_replicated_partitions", 0) > 0:
        findings.append({"severity": "high", "issue": "Cluster has under-replicated partitions."})
    if cluster.get("offline_partitions", 0) > 0:
        findings.append({"severity": "critical", "issue": "Cluster has offline partitions."})
    return findings
