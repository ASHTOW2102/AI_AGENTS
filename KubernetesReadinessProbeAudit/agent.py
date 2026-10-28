"""Review Kubernetes readiness/liveness probe configuration for safety."""
from typing import Any


def audit(workload: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not workload.get("readiness_probe"):
        findings.append({"severity": "high", "issue": "Workload has no readiness probe."})
    if not workload.get("liveness_probe"):
        findings.append({"severity": "medium", "issue": "Workload has no liveness probe."})
    if workload.get("liveness_initial_delay_seconds", 0) < workload.get("startup_duration_p99_seconds", 0):
        findings.append({"severity": "medium", "issue": "Liveness probe may run before startup completes."})
    if workload.get("readiness_failure_threshold", 0) < workload.get("min_readiness_failure_threshold", 1):
        findings.append({"severity": "low", "issue": "Readiness failure threshold is below the allowed minimum."})
    return findings
