"""Flags LLM agent pipelines that execute tool calls without validating arguments against the tool's schema."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pipeline.get("executes_tool_calls") and not pipeline.get("argument_schema_validated"):
        findings.append({"severity": "high", "issue": "Tool call arguments are executed without schema validation."})
    if pipeline.get("executes_tool_calls") and not pipeline.get("destructive_tools_require_confirmation"):
        findings.append({"severity": "high", "issue": "Destructive tool calls do not require confirmation."})
    return findings
