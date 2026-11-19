"""Flags feature flag rollouts that jump from a small percentage straight to 100%, skipping the staged increments that would catch a regression early."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    jump = flag.get("new_rollout_percent", 0) - flag.get("previous_rollout_percent", 0)
    if jump > flag.get("max_acceptable_jump_percent", 25):
        findings.append({"severity": "medium", "issue": "Rollout percentage jump exceeds the acceptable staged increment."})
    if flag.get("new_rollout_percent", 0) == 100 and flag.get("previous_rollout_percent", 0) < 50:
        findings.append({"severity": "high", "issue": "Rollout jumped to 100% without passing through a majority-exposure stage."})
    return findings
