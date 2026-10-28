"""Check Kubernetes resource requests and limits for workload containers."""
from typing import Any


def audit(workload: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for container in workload.get("containers", []):
        name = container.get("name", "<unnamed>")
        requests, limits = container.get("requests", {}), container.get("limits", {})
        for resource in ("cpu", "memory"):
            if resource not in requests:
                findings.append({"severity": "medium", "issue": f"{name} has no {resource} request."})
            if resource not in limits:
                findings.append({"severity": "medium", "issue": f"{name} has no {resource} limit."})
        if "memory" in requests and "memory" in limits and requests["memory"] > limits["memory"]:
            findings.append({"severity": "high", "issue": f"{name} memory request exceeds its limit."})
    return findings
