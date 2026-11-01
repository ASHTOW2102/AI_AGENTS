"""Checks GPU allocation efficiency and idle-time thresholds for training and inference workloads."""
from typing import Any


def audit(workload: dict[str, Any]):
    findings = []
    if workload.get("avg_utilization_percent", 100) < workload.get("min_expected_utilization_percent", 30):
        findings.append({"severity": "medium", "issue": "GPU utilization is below the expected minimum."})
    if workload.get("idle_hours_per_day", 0) > workload.get("max_idle_hours_per_day", 4) and not workload.get("autoscale_enabled"):
        findings.append({"severity": "medium", "issue": "GPU idles frequently without autoscaling enabled."})
    if workload.get("memory_oom_events", 0) > 0:
        findings.append({"severity": "high", "issue": "Workload experienced GPU memory out-of-memory events."})
    return findings
