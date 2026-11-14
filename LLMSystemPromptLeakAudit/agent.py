"""Flags LLM applications where the system prompt can be extracted through adversarial user input."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pipeline.get("system_prompt_contains_secrets"):
        findings.append({"severity": "high", "issue": "System prompt contains secrets that could be leaked if extracted."})
    if not pipeline.get("prompt_leak_mitigation_tested"):
        findings.append({"severity": "medium", "issue": "No testing has been done for system prompt extraction resistance."})
    return findings
