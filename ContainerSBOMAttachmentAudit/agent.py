"""Checks container images for attached, signed software-bill-of-materials attestations."""
from typing import Any


def audit(image: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not image.get("sbom_attached"):
        findings.append({"severity": "high", "issue": "Image has no attached SBOM."})
    if image.get("sbom_attached") and not image.get("sbom_signature_verified"):
        findings.append({"severity": "high", "issue": "Attached SBOM has no verified signature."})
    if image.get("sbom_attached") and image.get("sbom_age_days", 0) > image.get("image_age_days", 0) + 1:
        findings.append({"severity": "medium", "issue": "SBOM predates the image build, suggesting it is stale."})
    return findings
