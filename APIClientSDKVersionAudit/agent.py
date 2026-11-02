"""Checks client SDK version adoption against deprecation and minimum-support policy."""
from typing import Any


def audit(client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if client.get("sdk_version") in client.get("deprecated_versions", []):
        findings.append({"severity": "high", "issue": "Client uses a deprecated SDK version."})
    if client.get("sdk_age_days", 0) > client.get("max_supported_age_days", 365):
        findings.append({"severity": "medium", "issue": "Client SDK version is older than the support window."})
    if client.get("traffic_share_percent", 0) > 10 and client.get("sdk_version") in client.get("deprecated_versions", []):
        findings.append({"severity": "high", "issue": "A significant traffic share still uses a deprecated SDK."})
    return findings
