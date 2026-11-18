"""Flags container images whose software bill of materials (SBOM) is stale relative to the image's last rebuild."""
from typing import Any


def audit(image: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not image.get("sbom_present"):
        findings.append({"severity": "high", "issue": "Image has no software bill of materials."})
    if image.get("sbom_present") and image.get("sbom_age_days", 0) > image.get("image_age_days", 0):
        findings.append({"severity": "medium", "issue": "SBOM is older than the image itself, indicating it was not regenerated on rebuild."})
    return findings
