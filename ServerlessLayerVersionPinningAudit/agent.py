"""Flags serverless functions that reference a shared layer by a mutable alias instead of a pinned version."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if function.get("layer_reference_type") == "alias":
        findings.append({"severity": "medium", "issue": "Function references a layer by mutable alias rather than a pinned version."})
    if function.get("layer_reference_type") == "alias" and not function.get("layer_change_notifications_enabled"):
        findings.append({"severity": "low", "issue": "No notification is sent when the aliased layer version changes."})
    return findings
