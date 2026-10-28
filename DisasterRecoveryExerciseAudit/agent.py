"""Review disaster-recovery exercises for scope, timing, and evidence."""
from typing import Any


def audit(exercise: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if exercise.get("days_since_last_exercise", 0) > exercise.get("max_days_between_exercises", 365):
        findings.append({"severity": "high", "issue": "Disaster-recovery exercise is overdue."})
    missing = sorted(set(exercise.get("required_scenarios", [])) - set(exercise.get("tested_scenarios", [])))
    if missing:
        findings.append({"severity": "medium", "issue": "Required recovery scenarios were not exercised: " + ", ".join(missing)})
    if exercise.get("measured_recovery_minutes", 0) > exercise.get("target_recovery_minutes", 0):
        findings.append({"severity": "high", "issue": "Measured recovery time exceeded the target."})
    if not exercise.get("findings_owner_assigned") and exercise.get("open_findings", 0) > 0:
        findings.append({"severity": "medium", "issue": "Open exercise findings have no assigned owner."})
    return findings
