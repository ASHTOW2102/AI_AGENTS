"""Checks pod anti-affinity rules for single-node concentration risk on critical workloads."""
from typing import Any


def audit(workload: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if workload.get("critical") and not workload.get("anti_affinity_configured"):
        findings.append({"severity": "high", "issue": "Critical workload has no pod anti-affinity rule."})
    if workload.get("replica_count", 1) > 1 and workload.get("max_replicas_per_node", 1) >= workload.get("replica_count", 1):
        findings.append({"severity": "medium", "issue": "All replicas could be scheduled onto the same node."})
    if workload.get("critical") and not workload.get("topology_spread_zone_aware"):
        findings.append({"severity": "medium", "issue": "Critical workload is not spread across availability zones."})
    return findings
