"""Checks Kubernetes workloads for missing or misconfigured PodDisruptionBudgets."""
from typing import Any


def audit(workload: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if workload.get("replica_count", 1) > 1 and not workload.get("pdb_configured"):
        findings.append({"severity": "high", "issue": "Multi-replica workload has no PodDisruptionBudget."})
    if workload.get("pdb_configured") and workload.get("min_available", 0) >= workload.get("replica_count", 1):
        findings.append({"severity": "medium", "issue": "PodDisruptionBudget minAvailable allows zero voluntary disruptions."})
    return findings
