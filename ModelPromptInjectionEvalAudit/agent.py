"""Review prompt-injection evaluation coverage and safety regression metrics."""
from typing import Any


def audit(run: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if run.get("attack_cases", 0) < run.get("minimum_attack_cases", 1):
        findings.append({"severity": "medium", "issue": "Prompt-injection evaluation has insufficient attack cases."})
    if run.get("blocked_attack_rate_percent", 100) < run.get("minimum_blocked_attack_rate_percent", 95):
        findings.append({"severity": "high", "issue": "Blocked attack rate is below the evaluation target."})
    if run.get("unsafe_tool_calls", 0) > 0:
        findings.append({"severity": "critical", "issue": "Evaluation observed unsafe tool calls."})
    if run.get("days_since_last_eval", 0) > run.get("max_eval_age_days", 30):
        findings.append({"severity": "low", "issue": "Prompt-injection evaluation is stale."})
    return findings
