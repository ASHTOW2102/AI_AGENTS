"""Checks container base-image age against the organization's patch-currency policy."""
from typing import Any


def audit(image: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if image.get("base_image_age_days", 0) > image.get("max_base_image_age_days", 90):
        findings.append({"severity": "medium", "issue": "Base image is older than the patch-currency policy allows."})
    if image.get("base_image_pinned_by_digest") is False:
        findings.append({"severity": "medium", "issue": "Base image is referenced by mutable tag rather than digest."})
    if image.get("newer_patch_available") and not image.get("rebuild_scheduled"):
        findings.append({"severity": "low", "issue": "A newer base-image patch is available with no rebuild scheduled."})
    return findings
