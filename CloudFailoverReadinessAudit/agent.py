"""Audit cloud service failover readiness against recovery objectives."""
from __future__ import annotations

from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if service.get("regions", 0) < 2:
        findings.append({"severity": "high", "issue": "Service has no secondary region for failover."})
    if service.get("measured_rto_minutes", 0) > service.get("target_rto_minutes", 0):
        findings.append({"severity": "high", "issue": "Measured recovery time exceeds the RTO target."})
    if service.get("replication_lag_minutes", 0) > service.get("max_replication_lag_minutes", 0):
        findings.append({"severity": "high", "issue": "Replication lag exceeds the recovery-point tolerance."})
    if service.get("unavailable_dependencies"):
        findings.append({"severity": "medium", "issue": "Failover dependencies are not available in the recovery region."})
    if service.get("days_since_failover_exercise", 0) > 365:
        findings.append({"severity": "medium", "issue": "Failover exercise is more than one year old."})
    return findings
