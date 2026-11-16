"""Flags mobile apps that handle deep links without validating the link's origin or target before navigation."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("handles_deep_links") and not app.get("deep_link_origin_validated"):
        findings.append({"severity": "high", "issue": "Deep link handler does not validate the link's origin."})
    if app.get("handles_deep_links") and app.get("deep_link_can_trigger_sensitive_action") and not app.get("confirmation_required"):
        findings.append({"severity": "high", "issue": "Deep link can trigger a sensitive action without user confirmation."})
    return findings
