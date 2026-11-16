"""Flags cloud resources missing required ownership and cost-center tags needed for accountability and billing allocation."""
from typing import Any


def audit(resource: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    required = {"owner", "cost_center", "environment"}
    missing = required - set(resource.get("tags", {}).keys())
    if missing:
        findings.append({"severity": "low", "issue": f"Resource is missing required tags: {sorted(missing)}"})
    if resource.get("tags", {}).get("environment") == "production" and "owner" not in resource.get("tags", {}):
        findings.append({"severity": "medium", "issue": "Production resource has no owner tag."})
    return findings
