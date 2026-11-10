"""Flags LLM requests that silently truncate context when the input exceeds the model's context window."""
from typing import Any


def audit(request: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if request.get("input_tokens", 0) > request.get("context_window_tokens", 0):
        findings.append({"severity": "high", "issue": "Input token count exceeds the model's context window."})
    if request.get("truncation_applied") and not request.get("truncation_logged"):
        findings.append({"severity": "medium", "issue": "Context was truncated but the truncation was not logged."})
    return findings
