"""Flags anonymized datasets where a deterministic, unsalted transform makes re-identification via join attacks feasible."""
from typing import Any


def audit(dataset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if dataset.get("anonymization_method") == "deterministic_hash" and not dataset.get("salted"):
        findings.append({"severity": "high", "issue": "Deterministic unsalted hashing allows re-identification via rainbow table or join attack."})
    if not dataset.get("k_anonymity_evaluated"):
        findings.append({"severity": "medium", "issue": "Dataset has not been evaluated for k-anonymity against quasi-identifiers."})
    return findings
