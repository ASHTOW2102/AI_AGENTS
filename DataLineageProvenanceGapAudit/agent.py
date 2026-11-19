"""Flags derived datasets with no recorded lineage back to their source tables, making impact analysis and audits impossible."""
from typing import Any


def audit(dataset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if dataset.get("is_derived") and not dataset.get("lineage_recorded"):
        findings.append({"severity": "medium", "issue": "Derived dataset has no recorded lineage back to its sources."})
    if dataset.get("lineage_recorded") and not dataset.get("lineage_includes_transformation_logic"):
        findings.append({"severity": "low", "issue": "Lineage records sources but not the transformation logic applied."})
    return findings
