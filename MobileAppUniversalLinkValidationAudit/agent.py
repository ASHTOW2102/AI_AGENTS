"""Flags mobile apps that accept universal/app links without validating the signing team ID, letting another app hijack the link on a compromised or jailbroken device."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not app.get("validates_universal_link_team_id"):
        findings.append({"severity": "high", "issue": "App does not validate the signing team ID on incoming universal/app links."})
    return findings
