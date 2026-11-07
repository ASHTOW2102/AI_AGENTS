"""Audits mobile app permission requests for scope creep beyond declared feature needs."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    requested = set(app.get("requested_permissions", []))
    justified = set(app.get("justified_permissions", []))
    unjustified = requested - justified
    if unjustified:
        findings.append({"severity": "high", "issue": f"Requested permissions without justification: {sorted(unjustified)}"})
    if app.get("requests_background_location") and "background_location" not in justified:
        findings.append({"severity": "high", "issue": "Background location access is requested without justification."})
    return findings
