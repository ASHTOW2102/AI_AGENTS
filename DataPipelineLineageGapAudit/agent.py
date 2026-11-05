"""Checks ETL pipeline stages for lineage tracking gaps between source and destination datasets."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    untracked = sorted(set(pipeline.get("output_datasets", [])) - set(pipeline.get("lineage_tracked_datasets", [])))
    if untracked:
        findings.append({"severity": "medium", "issue": "Output datasets with no recorded lineage: " + ", ".join(untracked)})
    if pipeline.get("transforms_pii") and not pipeline.get("lineage_includes_transform_logic"):
        findings.append({"severity": "high", "issue": "Lineage for a PII-transforming stage omits the transform logic reference."})
    if pipeline.get("lineage_last_verified_days_ago", 0) > pipeline.get("max_verification_interval_days", 90):
        findings.append({"severity": "low", "issue": "Lineage records have not been verified recently."})
    return findings
