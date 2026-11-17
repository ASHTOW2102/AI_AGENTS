"""Flags containers with liveness probes misconfigured to restart the container on transient slowness rather than true deadlock."""
from typing import Any


def audit(container: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if container.get("liveness_timeout_seconds", 0) < container.get("p99_response_time_seconds", 0):
        findings.append({"severity": "high", "issue": "Liveness probe timeout is shorter than the observed p99 response time, risking spurious restarts."})
    if not container.get("liveness_probe_configured"):
        findings.append({"severity": "medium", "issue": "Container has no liveness probe configured."})
    return findings
