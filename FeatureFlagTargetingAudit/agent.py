"""Review feature-flag targeting rules for safe cohort boundaries."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flag.get("production_enabled") and flag.get("rollout_percent", 0) > flag.get("approved_rollout_percent", 100):
        findings.append({"severity": "high", "issue": "Rollout percentage exceeds its approved limit."})
    if flag.get("targeting_uses_user_id") and not flag.get("stable_hash_assignment"):
        findings.append({"severity": "medium", "issue": "User targeting lacks stable cohort assignment."})
    if flag.get("targeting_filters") and not flag.get("targeting_owner"):
        findings.append({"severity": "low", "issue": "Targeting rules have no accountable owner."})
    if flag.get("kill_switch_required") and not flag.get("kill_switch_tested"):
        findings.append({"severity": "high", "issue": "Required kill switch has not been tested."})
    return findings
