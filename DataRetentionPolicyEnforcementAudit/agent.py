"""Flags datasets with a defined retention policy that is not actually enforced by automated deletion."""
from typing import Any


def audit(dataset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if dataset.get("retention_policy_days") and not dataset.get("automated_deletion_enabled"):
        findings.append({"severity": "high", "issue": "Retention policy is defined but not enforced by automated deletion."})
    if dataset.get("automated_deletion_enabled") and dataset.get("last_deletion_run_days_ago", 0) > dataset.get("expected_run_interval_days", 30):
        findings.append({"severity": "medium", "issue": "Automated deletion job has not run within the expected interval."})
    return findings
