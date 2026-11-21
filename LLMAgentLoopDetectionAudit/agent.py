"""Flags autonomous LLM agents with no detection for repeating the same tool call in a loop, risking runaway cost or action spam."""
from typing import Any


def audit(agent: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not agent.get("repeated_action_detection_enabled"):
        findings.append({"severity": "high", "issue": "Agent has no detection for repeating the same action in a loop."})
    if not agent.get("max_steps_per_task_enforced"):
        findings.append({"severity": "medium", "issue": "Agent has no hard cap on steps per task."})
    return findings
