"""Flags LLM agents whose available tool functions grant more privilege than the agent's declared task requires."""
from typing import Any


def audit(agent: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    excess = set(agent.get("available_tools", [])) - set(agent.get("required_tools_for_task", []))
    high_risk_excess = excess & set(agent.get("high_risk_tools", []))
    if high_risk_excess:
        findings.append({"severity": "high", "issue": f"Agent has access to unneeded high-risk tools: {sorted(high_risk_excess)}"})
    if not agent.get("tool_access_scoped_per_task"):
        findings.append({"severity": "medium", "issue": "Tool access is not scoped per task; the agent has standing access to all tools."})
    return findings
