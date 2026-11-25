"""Flags mobile apps handling sensitive data with no root/jailbreak detection, or whose detection is client-side only and trivially bypassable by hooking."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("handles_sensitive_data") and not app.get("checks_root_status"):
        findings.append({"severity": "high", "issue": "App handles sensitive data with no root/jailbreak detection."})
    elif app.get("checks_root_status") and app.get("root_check_is_client_side_only"):
        findings.append({"severity": "medium", "issue": "Root/jailbreak check is client-side only and can be bypassed by hooking."})
    return findings
