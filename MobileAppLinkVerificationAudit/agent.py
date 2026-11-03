"""Checks mobile universal/app-link domain verification to prevent link hijacking."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not app.get("assetlinks_or_aasa_published"):
        findings.append({"severity": "high", "issue": "Domain has no published app-association file."})
    if app.get("assetlinks_or_aasa_published") and not app.get("package_fingerprint_matches"):
        findings.append({"severity": "high", "issue": "Published association file does not match the app's signing fingerprint."})
    if app.get("link_handling_mode") == "always_open_in_app" and not app.get("verification_enforced"):
        findings.append({"severity": "medium", "issue": "App claims links without enforced domain verification."})
    return findings
