"""Flags auto scaling groups whose max capacity is not greater than min capacity, meaning no actual scaling range exists despite the policy."""
from typing import Any


def audit(asg: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    min_capacity = asg.get("min_capacity", 0)
    max_capacity = asg.get("max_capacity", 0)
    if max_capacity <= min_capacity:
        findings.append({"severity": "medium", "issue": f"Max capacity ({max_capacity}) is not greater than min capacity ({min_capacity}); no real scaling range."})
    return findings
