"""Flags container images with no verifiable build provenance attestation linking them to source and build pipeline."""
from typing import Any


def audit(image: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not image.get("provenance_attestation_present"):
        findings.append({"severity": "high", "issue": "Image has no build provenance attestation."})
    if image.get("provenance_attestation_present") and not image.get("builder_identity_verified"):
        findings.append({"severity": "medium", "issue": "Provenance attestation exists but builder identity is not verified."})
    return findings
