"""Flags Kubernetes pods with no ephemeral storage limit, letting log or scratch writes fill the node disk and evict other workloads."""
from typing import Any


def audit(pod: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not pod.get("ephemeral_storage_limit_set"):
        findings.append({"severity": "high", "issue": "Pod has no ephemeral storage limit set."})
    if pod.get("writes_large_temp_files") and pod.get("ephemeral_storage_limit_set") and pod.get("ephemeral_storage_limit_mb", 0) < pod.get("expected_temp_usage_mb", 0):
        findings.append({"severity": "medium", "issue": "Ephemeral storage limit is set below the workload's expected temp file usage."})
    return findings
