"""Checks third-party script tags for subresource integrity and safe loading attributes."""
from typing import Any


def audit(script: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if script.get("third_party") and not script.get("integrity_hash"):
        findings.append({"severity": "high", "issue": "Third-party script has no subresource integrity hash."})
    if script.get("third_party") and script.get("crossorigin") != "anonymous":
        findings.append({"severity": "medium", "issue": "Third-party script does not set crossorigin=anonymous."})
    if script.get("loaded_over_http"):
        findings.append({"severity": "critical", "issue": "Script is loaded over plain HTTP."})
    return findings
