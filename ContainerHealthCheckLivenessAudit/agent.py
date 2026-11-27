"""Flags containers with no liveness probe configured (so a hung process is never restarted) or no readiness probe (so traffic reaches a container before it's ready)."""
from typing import Any


def audit(container: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not container.get("liveness_probe_configured"):
        findings.append({"severity": "high", "issue": "No liveness probe configured; a hung process is never restarted."})
    if not container.get("readiness_probe_configured"):
        findings.append({"severity": "medium", "issue": "No readiness probe configured; traffic can reach the container before it's ready."})
    return findings
