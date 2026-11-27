"""Flags Kubernetes clusters with no pod security admission control enabled, allowing any pod spec including privileged ones to be scheduled."""
from typing import Any


def audit(cluster: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not cluster.get("pod_security_admission_enabled"):
        findings.append({"severity": "high", "issue": "Cluster has no pod security admission control enabled."})
    return findings
