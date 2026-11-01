"""Checks model-registry entries for approval status, lineage, and promotion evidence."""
from typing import Any


def audit(model: dict[str, Any]):
    findings = []
    if model.get("stage") == "production" and not model.get("approved_by"):
        findings.append({"severity": "critical", "issue": "Production model has no recorded approver."})
    if not model.get("training_data_reference"):
        findings.append({"severity": "high", "issue": "Model has no training-data lineage reference."})
    if model.get("stage") == "production" and not model.get("evaluation_report_reference"):
        findings.append({"severity": "high", "issue": "Production model has no evaluation report on file."})
    return findings
