"""Checks LLM prompt assembly for context-window budget overruns and truncation safety."""
from typing import Any


def audit(request: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if request.get("estimated_tokens", 0) > request.get("model_context_limit", 0):
        findings.append({"severity": "high", "issue": "Estimated prompt tokens exceed the model's context window."})
    if request.get("truncation_possible") and not request.get("truncation_preserves_instructions"):
        findings.append({"severity": "high", "issue": "Truncation under budget pressure may drop system instructions."})
    if request.get("reserved_output_tokens", 0) < request.get("min_reserved_output_tokens", 0):
        findings.append({"severity": "medium", "issue": "Too few tokens are reserved for the model's output."})
    return findings
