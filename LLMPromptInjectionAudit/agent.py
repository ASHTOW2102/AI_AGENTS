"""Flags LLM pipelines that lack isolation between trusted instructions and untrusted retrieved content."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pipeline.get("untrusted_content_in_prompt") and not pipeline.get("content_delimiting_enforced"):
        findings.append({"severity": "high", "issue": "Untrusted content is mixed into the prompt without delimiting."})
    if not pipeline.get("output_action_allowlist"):
        findings.append({"severity": "medium", "issue": "Model output can trigger actions without an allowlist check."})
    return findings
