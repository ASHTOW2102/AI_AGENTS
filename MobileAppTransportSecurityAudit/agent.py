"""Review mobile transport policy for cleartext exceptions and trust overrides."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("cleartext_traffic_enabled"):
        findings.append({"severity": "high", "issue": "Mobile app permits cleartext network traffic."})
    if app.get("trust_all_certificates"):
        findings.append({"severity": "critical", "issue": "App trusts all server certificates."})
    if app.get("debug_trust_override_in_release"):
        findings.append({"severity": "critical", "issue": "Debug certificate trust override is enabled in release."})
    if app.get("exception_domains") and not app.get("exception_domains_reviewed"):
        findings.append({"severity": "medium", "issue": "Transport-security exception domains have not been reviewed."})
    return findings
