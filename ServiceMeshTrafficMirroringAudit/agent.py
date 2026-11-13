"""Flags service mesh traffic mirroring configurations that forward production payloads to non-production environments without sanitization."""
from typing import Any


def audit(mesh: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if mesh.get("mirrors_to_nonprod") and not mesh.get("payload_sanitized"):
        findings.append({"severity": "high", "issue": "Production traffic is mirrored to non-production without payload sanitization."})
    if mesh.get("mirrors_to_nonprod") and not mesh.get("mirroring_percentage_capped"):
        findings.append({"severity": "low", "issue": "Traffic mirroring percentage is uncapped."})
    return findings
