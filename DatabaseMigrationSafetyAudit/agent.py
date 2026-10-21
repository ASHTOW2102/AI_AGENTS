"""Review database migration deployment safety metadata."""
from typing import Any


def audit(migration: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if migration.get("destructive") and not migration.get("backup_verified"):
        findings.append({"severity": "critical", "issue": "Destructive migration has no verified backup."})
    if migration.get("estimated_lock_seconds", 0) > migration.get("max_lock_seconds", 0):
        findings.append({"severity": "high", "issue": "Estimated lock duration exceeds the deployment limit."})
    if migration.get("requires_backfill") and not migration.get("backfill_throttled"):
        findings.append({"severity": "medium", "issue": "Backfill has no throttling control."})
    if migration.get("rollback_supported") is False and not migration.get("forward_fix_plan"):
        findings.append({"severity": "high", "issue": "Non-reversible migration has no forward-fix plan."})
    if not migration.get("staging_rehearsed"):
        findings.append({"severity": "medium", "issue": "Migration has not been rehearsed in staging."})
    return findings
