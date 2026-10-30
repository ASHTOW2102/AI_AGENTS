"""Review multi-region service readiness and dependency failover coverage."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if service.get("regions", 0) < 2 and service.get("multi_region_required"):
        findings.append({"severity": "high", "issue": "Service has fewer than two configured regions."})
    missing = sorted(set(service.get("critical_dependencies", [])) - set(service.get("failover_dependencies", [])))
    if missing:
        findings.append({"severity": "high", "issue": "Failover region lacks dependencies: " + ", ".join(missing)})
    if service.get("failover_enabled") and not service.get("traffic_switch_tested"):
        findings.append({"severity": "medium", "issue": "Traffic switching has not been tested."})
    if service.get("measured_failover_minutes", 0) > service.get("target_failover_minutes", 0):
        findings.append({"severity": "medium", "issue": "Measured failover time exceeds target."})
    return findings
