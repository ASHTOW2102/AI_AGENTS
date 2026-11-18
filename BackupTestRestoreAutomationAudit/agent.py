"""Flags backup systems that rely on manual restore drills instead of an automated, regularly scheduled restore test."""
from typing import Any


def audit(backup: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not backup.get("automated_restore_test_enabled"):
        findings.append({"severity": "high", "issue": "Restore testing is manual, not automated and regularly scheduled."})
    if backup.get("automated_restore_test_enabled") and backup.get("days_since_last_successful_test", 0) > backup.get("max_acceptable_test_interval_days", 30):
        findings.append({"severity": "medium", "issue": "Automated restore test has not succeeded within the acceptable interval."})
    return findings
