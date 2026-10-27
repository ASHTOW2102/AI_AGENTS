"""Check backup and replication recovery-point objectives against evidence."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if service.get("measured_data_loss_minutes", 0) > service.get("target_rpo_minutes", 0):
        findings.append({"severity": "high", "issue": "Measured recovery point exceeds the RPO target."})
    if service.get("backup_interval_minutes", 0) > service.get("target_rpo_minutes", 0):
        findings.append({"severity": "high", "issue": "Backup interval cannot meet the configured RPO."})
    if not service.get("recovery_point_tested"):
        findings.append({"severity": "medium", "issue": "Recovery point has not been validated in a restore test."})
    if service.get("replication_lag_minutes", 0) > service.get("target_rpo_minutes", 0):
        findings.append({"severity": "medium", "issue": "Replication lag exceeds the recovery-point objective."})
    return findings
