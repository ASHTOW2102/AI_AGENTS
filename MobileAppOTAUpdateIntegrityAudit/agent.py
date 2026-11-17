"""Flags mobile apps that apply over-the-air code updates without verifying a cryptographic signature on the update bundle."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("supports_ota_updates") and not app.get("ota_bundle_signature_verified"):
        findings.append({"severity": "high", "issue": "OTA update bundle signature is not verified before being applied."})
    if app.get("ota_bundle_signature_verified") and not app.get("rollback_on_verification_failure"):
        findings.append({"severity": "medium", "issue": "No rollback occurs if OTA signature verification fails."})
    return findings
