"""Flags fully-rolled-out feature flags that remain in the codebase long past their cleanup deadline."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flag.get("rollout_percent", 0) >= 100 and flag.get("days_since_full_rollout", 0) > flag.get("max_cleanup_days", 60):
        findings.append({"severity": "low", "issue": "Fully rolled-out flag is overdue for code cleanup."})
    if flag.get("rollout_percent", 0) >= 100 and not flag.get("cleanup_ticket_filed"):
        findings.append({"severity": "low", "issue": "No cleanup ticket has been filed for this fully-rolled-out flag."})
    return findings
