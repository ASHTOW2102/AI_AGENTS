"""Flags serverless functions whose IAM execution role grants broader permissions than the function's declared actions require."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    excess = set(function.get("granted_actions", [])) - set(function.get("used_actions", []))
    if excess:
        findings.append({"severity": "medium", "issue": f"Function role grants unused actions: {sorted(excess)}"})
    if "*" in function.get("granted_actions", []):
        findings.append({"severity": "high", "issue": "Function role grants wildcard permissions."})
    return findings
