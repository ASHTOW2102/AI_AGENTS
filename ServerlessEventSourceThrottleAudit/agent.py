"""Flags serverless functions with event source mappings lacking concurrency throttles against downstream overload."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not function.get("max_concurrency_configured"):
        findings.append({"severity": "high", "issue": "Event source mapping has no maximum concurrency limit."})
    if function.get("max_concurrency_configured") and function.get("downstream_max_connections", 0) < function.get("configured_max_concurrency", 0):
        findings.append({"severity": "medium", "issue": "Configured concurrency exceeds downstream connection capacity."})
    return findings
