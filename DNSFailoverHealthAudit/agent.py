"""Review DNS failover health-check coverage and failback readiness."""
from typing import Any


def audit(zone: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if zone.get("failover_enabled") and not zone.get("health_check_configured"):
        findings.append({"severity": "high", "issue": "DNS failover is enabled without a health check."})
    if zone.get("health_check_configured") and not zone.get("health_check_multi_region"):
        findings.append({"severity": "medium", "issue": "Health check lacks an independent monitoring region."})
    if zone.get("failover_enabled") and not zone.get("failback_tested"):
        findings.append({"severity": "medium", "issue": "Failback behavior has not been tested."})
    if zone.get("health_check_interval_seconds", 0) > zone.get("max_health_check_interval_seconds", 60):
        findings.append({"severity": "low", "issue": "Health-check interval exceeds the detection objective."})
    return findings
