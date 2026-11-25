"""Flags API keys granted scopes beyond the minimum their intended use actually requires."""
from typing import Any


def audit(api_key: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    granted = set(api_key.get("granted_scopes", []))
    minimum = set(api_key.get("minimum_required_scopes", []))
    extra = granted - minimum
    if extra:
        findings.append({"severity": "high", "issue": f"API key is granted scopes beyond the minimum required: {sorted(extra)}"})
    return findings
