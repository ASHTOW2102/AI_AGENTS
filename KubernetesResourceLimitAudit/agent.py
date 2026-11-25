"""Flags Kubernetes pods whose containers have no CPU or memory limit set, letting a single misbehaving container starve the whole node."""
from typing import Any


def audit(pod: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    unbounded = [c.get("name", "?") for c in pod.get("containers", []) if not c.get("cpu_limit") or not c.get("memory_limit")]
    if unbounded:
        findings.append({"severity": "high", "issue": f"Containers with no CPU and/or memory limit: {unbounded}"})
    return findings
