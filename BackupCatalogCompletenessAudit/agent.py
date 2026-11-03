"""Checks backup catalog entries for missing scheduled jobs and untracked data stores."""
from typing import Any


def audit(catalog: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    untracked = sorted(set(catalog.get("data_stores", [])) - set(catalog.get("backed_up_stores", [])))
    if untracked:
        findings.append({"severity": "high", "issue": "Data stores with no backup coverage: " + ", ".join(untracked)})
    if catalog.get("backup_jobs_missing_schedule", 0) > 0:
        findings.append({"severity": "medium", "issue": "Some backup jobs have no defined schedule."})
    if catalog.get("last_catalog_audit_days_ago", 0) > catalog.get("max_audit_interval_days", 90):
        findings.append({"severity": "low", "issue": "Backup catalog has not been audited recently."})
    return findings
