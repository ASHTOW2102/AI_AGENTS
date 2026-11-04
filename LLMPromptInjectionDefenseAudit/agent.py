"""Checks LLM pipelines handling untrusted input for prompt-injection defenses and privilege separation."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pipeline.get("processes_untrusted_input") and not pipeline.get("input_output_delimited"):
        findings.append({"severity": "high", "issue": "Untrusted input is not clearly delimited from trusted instructions."})
    if pipeline.get("model_has_tool_access") and pipeline.get("processes_untrusted_input") and not pipeline.get("tool_calls_require_confirmation"):
        findings.append({"severity": "critical", "issue": "Model with tool access processes untrusted input without confirmation gating."})
    if pipeline.get("system_prompt_contains_secrets"):
        findings.append({"severity": "high", "issue": "System prompt embeds secrets that could leak via injection."})
    return findings
