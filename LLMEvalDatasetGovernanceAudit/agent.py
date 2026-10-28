"""Review evaluation dataset governance, provenance, and leakage controls."""
from typing import Any


def audit(dataset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not dataset.get("source_documented"):
        findings.append({"severity": "medium", "issue": "Evaluation dataset source is undocumented."})
    if dataset.get("contains_personal_data") and not dataset.get("deidentified"):
        findings.append({"severity": "high", "issue": "Evaluation data contains personal information without de-identification."})
    if dataset.get("train_eval_overlap_possible") and not dataset.get("overlap_checked"):
        findings.append({"severity": "high", "issue": "Train/evaluation overlap risk has not been checked."})
    if not dataset.get("versioned"):
        findings.append({"severity": "low", "issue": "Evaluation dataset is not versioned for reproducibility."})
    return findings
