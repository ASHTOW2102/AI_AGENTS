"""Flags serverless function execution roles whose policy grants access to a wildcard resource instead of a scoped ARN."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if function.get("iam_role_allows_wildcard_resource"):
        findings.append({"severity": "high", "issue": "Function execution role grants access to a wildcard resource."})
    return findings
