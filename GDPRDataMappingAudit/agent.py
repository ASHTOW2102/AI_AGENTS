"""Checks personal-data processing records for legal basis, purpose, and transfer safeguards."""
from typing import Any


def audit(record: dict[str, Any]):
    findings = []
    if not record.get("legal_basis"):
        findings.append({"severity": "high", "issue": "Processing record has no documented legal basis."})
    if not record.get("purpose"):
        findings.append({"severity": "medium", "issue": "Processing record has no stated purpose."})
    if record.get("cross_border_transfer") and not record.get("transfer_safeguard"):
        findings.append({"severity": "high", "issue": "Cross-border transfer has no documented safeguard."})
    if record.get("third_party_sharing") and not record.get("data_processing_agreement"):
        findings.append({"severity": "high", "issue": "Third-party sharing has no data processing agreement."})
    return findings
