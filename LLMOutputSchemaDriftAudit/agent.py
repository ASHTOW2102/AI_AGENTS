"""Flags LLM pipelines whose structured output has drifted from the expected schema without the application detecting it."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pipeline.get("schema_validation_failures_last_24h", 0) > 0 and not pipeline.get("validation_failures_alerted"):
        findings.append({"severity": "high", "issue": "Schema validation failures occurred but were not alerted on."})
    if not pipeline.get("output_schema_validated"):
        findings.append({"severity": "high", "issue": "LLM output is not validated against an expected schema at all."})
    return findings
