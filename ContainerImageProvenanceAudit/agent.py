"""Flags container deployments that pull images without verifying signed provenance (e.g. Sigstore/cosign attestation), allowing an unsigned or tampered image to be deployed undetected."""
from typing import Any


def audit(deployment: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    verifies_signature = deployment.get("verifies_image_signature", False)
    enforces_at_admission = deployment.get("enforces_signature_at_admission", False)

    if not verifies_signature:
        findings.append({"severity": "high", "issue": "Deployment pulls container images without verifying a signed provenance attestation, so a tampered or unsigned image can be deployed undetected."})
    elif not enforces_at_admission:
        findings.append({"severity": "medium", "issue": "Signature verification exists but is not enforced at cluster admission, so an unsigned image could still be scheduled if the check is bypassed."})
    return findings
