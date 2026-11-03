"""Checks API version negotiation for explicit client opt-in and safe default behavior."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("version_specified_by_client"):
        findings.append({"severity": "medium", "issue": "Clients do not explicitly specify an API version."})
    if endpoint.get("default_version_changes_without_notice"):
        findings.append({"severity": "high", "issue": "The default API version can change without client notice."})
    if endpoint.get("unsupported_version_requested") and endpoint.get("silently_downgrades"):
        findings.append({"severity": "high", "issue": "Unsupported version requests are silently downgraded instead of erroring."})
    return findings
