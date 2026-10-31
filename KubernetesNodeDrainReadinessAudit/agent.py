"""Review Kubernetes node-drain readiness and workload eviction safeguards."""
from typing import Any


def audit(node: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if node.get("critical_workloads", 0) > 0 and not node.get("pod_disruption_budget_coverage"):
        findings.append({"severity": "high", "issue": "Critical workloads lack disruption-budget coverage."})
    if node.get("daemonsets_unmanaged"):
        findings.append({"severity": "medium", "issue": "Drain behavior for required daemonsets is not configured."})
    if node.get("local_storage_workloads", 0) > 0 and not node.get("local_data_drain_plan"):
        findings.append({"severity": "high", "issue": "Node hosts local-storage workloads without a drain plan."})
    if node.get("max_unavailable_nodes", 0) > node.get("approved_max_unavailable_nodes", 1):
        findings.append({"severity": "medium", "issue": "Concurrent node drain limit exceeds policy."})
    return findings
