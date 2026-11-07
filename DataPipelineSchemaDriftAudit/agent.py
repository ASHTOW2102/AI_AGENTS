"""Flags data pipelines where upstream schema drift is not caught before downstream consumption."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pipeline.get("upstream_schema_changed") and not pipeline.get("schema_validation_enabled"):
        findings.append({"severity": "high", "issue": "Upstream schema changed with no validation gate before downstream load."})
    if not pipeline.get("schema_change_alerting"):
        findings.append({"severity": "medium", "issue": "No alerting is configured for upstream schema changes."})
    return findings
