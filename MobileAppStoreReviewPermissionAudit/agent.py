"""Checks requested mobile app permissions against stated purpose for store-review and privacy risk."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    undeclared = sorted(set(app.get("requested_permissions", [])) - set(app.get("declared_purposes", {}).keys()))
    if undeclared:
        findings.append({"severity": "high", "issue": "Permissions requested with no declared purpose: " + ", ".join(undeclared)})
    if app.get("requests_permission_at_launch") and not app.get("just_in_time_prompt"):
        findings.append({"severity": "medium", "issue": "Sensitive permissions are requested at launch rather than just-in-time."})
    if app.get("background_location_requested") and not app.get("background_location_justified"):
        findings.append({"severity": "high", "issue": "Background location access has no documented justification."})
    return findings
