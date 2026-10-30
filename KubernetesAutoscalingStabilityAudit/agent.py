"""Review Kubernetes autoscaling bounds and stabilization configuration."""
from typing import Any


def audit(scaler: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if scaler.get("min_replicas", 0) > scaler.get("max_replicas", 0):
        findings.append({"severity": "high", "issue": "Minimum replicas exceed maximum replicas."})
    if scaler.get("scale_down_stabilization_seconds", 0) < scaler.get("min_scale_down_stabilization_seconds", 0):
        findings.append({"severity": "medium", "issue": "Scale-down stabilization is shorter than policy."})
    if not scaler.get("metrics_available"):
        findings.append({"severity": "high", "issue": "Autoscaler has no available metrics source."})
    if scaler.get("max_replicas", 0) > scaler.get("capacity_supported_replicas", float("inf")):
        findings.append({"severity": "medium", "issue": "Autoscaler maximum exceeds supported backend capacity."})
    return findings
