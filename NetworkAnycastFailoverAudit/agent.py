"""Flags anycast-routed services with no verified failover path when the nearest point of presence becomes unhealthy."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not service.get("failover_path_verified"):
        findings.append({"severity": "high", "issue": "Anycast failover path has never been verified."})
    if service.get("failover_path_verified") and service.get("failover_time_seconds", 0) > service.get("max_acceptable_failover_seconds", 30):
        findings.append({"severity": "medium", "issue": "Anycast failover time exceeds the acceptable threshold."})
    return findings
