"""Checks container image signing certificates for expiry and missing signature verification."""
from typing import Any


def audit(image: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not image.get("signature_present"):
        findings.append({"severity": "high", "issue": "Container image has no cryptographic signature."})
    if image.get("signature_present") and image.get("signature_expired"):
        findings.append({"severity": "high", "issue": "Container image signature has expired."})
    if image.get("signature_present") and not image.get("verification_enforced"):
        findings.append({"severity": "medium", "issue": "Signature exists but verification is not enforced at deploy time."})
    return findings
