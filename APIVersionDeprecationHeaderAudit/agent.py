"""Checks that deprecated API responses carry standard deprecation and sunset headers."""
from typing import Any


def audit(response: dict[str, Any]):
    findings = []
    if response.get("deprecated") and "Deprecation" not in response.get("headers", {}):
        findings.append({"severity": "medium", "issue": "Deprecated response has no Deprecation header."})
    if response.get("deprecated") and "Sunset" not in response.get("headers", {}):
        findings.append({"severity": "medium", "issue": "Deprecated response has no Sunset header."})
    if response.get("deprecated") and "Link" not in response.get("headers", {}):
        findings.append({"severity": "low", "issue": "Deprecated response has no successor Link header."})
    return findings
