"""Flags data pipeline stages that consume upstream data without schema validation, allowing silent schema drift (renamed, removed, or retyped columns) to corrupt downstream data."""
from typing import Any


def audit(stage: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    validates_schema = stage.get("validates_input_schema", False)
    fails_on_mismatch = stage.get("fails_closed_on_schema_mismatch", False)

    if not validates_schema:
        findings.append({"severity": "high", "issue": "Pipeline stage does not validate the input schema, so upstream column renames, removals, or type changes can silently corrupt downstream data."})
    elif not fails_on_mismatch:
        findings.append({"severity": "medium", "issue": "Schema validation exists but does not fail closed on mismatch, so drift may be logged but still allowed through."})
    return findings
