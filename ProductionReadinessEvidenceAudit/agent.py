"""Check whether a release has core operational readiness evidence."""
from typing import Any


def audit(release: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for field, label in (("rollback_plan", "rollback plan"), ("runbook", "runbook"),
                         ("owner", "service owner"), ("health_checks", "health checks")):
        if not release.get(field):
            findings.append({"severity": "medium", "issue": f"Release has no recorded {label}."})
    if release.get("data_migration") and not release.get("migration_recovery_plan"):
        findings.append({"severity": "high", "issue": "Release includes a data migration without a recovery plan."})
    if release.get("known_critical_findings", 0) > 0 and not release.get("risk_acceptance_reference"):
        findings.append({"severity": "high", "issue": "Known critical findings lack a risk-acceptance reference."})
    return findings
