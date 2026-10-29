"""Review dataset de-identification controls for linkage and re-identification risk."""
from typing import Any


def audit(dataset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if dataset.get("direct_identifiers_present"):
        findings.append({"severity": "critical", "issue": "Dataset retains direct personal identifiers."})
    if dataset.get("quasi_identifiers_count", 0) > 0 and not dataset.get("linkage_risk_assessed"):
        findings.append({"severity": "high", "issue": "Quasi-identifier linkage risk has not been assessed."})
    if dataset.get("pseudonymized") and not dataset.get("mapping_key_separated"):
        findings.append({"severity": "high", "issue": "Pseudonymization mapping key is not stored separately."})
    if not dataset.get("reidentification_tested"):
        findings.append({"severity": "medium", "issue": "De-identification has no recorded re-identification test."})
    return findings
