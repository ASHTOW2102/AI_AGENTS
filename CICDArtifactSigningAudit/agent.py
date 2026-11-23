"""Flags CI/CD pipelines that publish build artifacts to a public registry without cryptographically signing them, allowing undetected tampering."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pipeline.get("publishes_to_public_registry") and not pipeline.get("artifact_signing_enabled"):
        findings.append({"severity": "high", "issue": "Pipeline publishes artifacts to a public registry without signing them."})
    return findings
