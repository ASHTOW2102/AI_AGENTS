"""Checks liveness probe configuration for restart-loop risk and dependency-coupling mistakes."""
from typing import Any


def audit(workload: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not workload.get("liveness_probe_configured"):
        findings.append({"severity": "high", "issue": "Workload has no liveness probe configured."})
    if workload.get("liveness_probe_checks_downstream_dependency"):
        findings.append({"severity": "high", "issue": "Liveness probe fails when an unrelated downstream dependency is unhealthy."})
    if workload.get("liveness_probe_configured") and workload.get("initial_delay_seconds", 0) < workload.get("startup_time_seconds", 0):
        findings.append({"severity": "medium", "issue": "Liveness probe can fire before the workload finishes starting up."})
    return findings
