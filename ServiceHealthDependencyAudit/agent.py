"""Review service health-check dependency and degradation policy."""
from typing import Any


def audit(health: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if health.get("readiness_depends_on_optional_services"):
        findings.append({"severity": "medium", "issue": "Readiness depends on an optional downstream service."})
    if health.get("liveness_checks_downstream"):
        findings.append({"severity": "high", "issue": "Liveness probe can restart the service due to downstream failure."})
    if not health.get("dependency_timeout_seconds"):
        findings.append({"severity": "medium", "issue": "Health-check dependency calls have no timeout."})
    if health.get("degraded_mode_supported") and not health.get("degraded_mode_health_semantics"):
        findings.append({"severity": "low", "issue": "Health status during degraded mode is undefined."})
    return findings
