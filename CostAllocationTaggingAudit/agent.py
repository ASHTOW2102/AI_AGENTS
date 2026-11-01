"""Checks cloud resource tagging completeness for cost-allocation and ownership reporting."""
from typing import Any


def audit(resource: dict[str, Any]):
    findings = []
    required = {"owner", "cost_center", "environment"}
    missing = sorted(required - set(resource.get("tags", {}).keys()))
    if missing:
        findings.append({"severity": "medium", "issue": "Missing required cost tags: " + ", ".join(missing)})
    if resource.get("monthly_cost", 0) > resource.get("untagged_alert_threshold", 1000) and missing:
        findings.append({"severity": "high", "issue": "High-cost resource is missing cost-allocation tags."})
    return findings
