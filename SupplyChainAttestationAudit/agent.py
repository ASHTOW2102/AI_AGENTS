"""Check artifact records for signed supply-chain attestation evidence."""
from typing import Any


def audit(artifact: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not artifact.get("attestation_present"):
        findings.append({"severity": "high", "issue": "Build artifact has no supply-chain attestation."})
    if artifact.get("attestation_present") and not artifact.get("signature_verified"):
        findings.append({"severity": "critical", "issue": "Attestation signature is not verified."})
    if not artifact.get("source_revision"):
        findings.append({"severity": "medium", "issue": "Artifact is not linked to a source revision."})
    if not artifact.get("builder_identity") or artifact.get("builder_identity") not in artifact.get("approved_builders", []):
        findings.append({"severity": "high", "issue": "Artifact builder is missing or not approved."})
    return findings
