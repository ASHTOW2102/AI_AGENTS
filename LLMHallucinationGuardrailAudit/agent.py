"""Checks LLM answer pipelines for grounding checks and uncertainty signaling to reduce hallucination risk."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pipeline.get("answers_from_retrieval") and not pipeline.get("groundedness_check_applied"):
        findings.append({"severity": "high", "issue": "Retrieval-based answers are not checked for groundedness against sources."})
    if pipeline.get("high_stakes_domain") and not pipeline.get("confidence_or_uncertainty_surfaced"):
        findings.append({"severity": "high", "issue": "High-stakes answers surface no confidence or uncertainty signal."})
    if pipeline.get("groundedness_check_applied") and not pipeline.get("fallback_on_low_groundedness"):
        findings.append({"severity": "medium", "issue": "Low-groundedness answers have no defined fallback behavior."})
    return findings
