"""Flags web pages that load third-party scripts without Subresource Integrity hashes."""
from typing import Any


def audit(page: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    unprotected = [s for s in page.get("third_party_scripts", []) if s not in page.get("sri_protected_scripts", [])]
    if unprotected:
        findings.append({"severity": "high", "issue": f"Third-party scripts without SRI hashes: {unprotected}"})
    if page.get("third_party_scripts") and not page.get("crossorigin_attribute_set"):
        findings.append({"severity": "low", "issue": "Third-party scripts lack the crossorigin attribute needed for SRI reporting."})
    return findings
