"""Flags container images that exceed a recommended size budget, slowing pulls and increasing attack surface."""
from typing import Any


def audit(image: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if image.get("size_mb", 0) > image.get("max_acceptable_size_mb", 500):
        findings.append({"severity": "medium", "issue": "Image size exceeds the recommended budget."})
    if image.get("uses_full_os_base_image") and image.get("size_mb", 0) > 200:
        findings.append({"severity": "low", "issue": "Large image built on a full OS base rather than a minimal base."})
    return findings
