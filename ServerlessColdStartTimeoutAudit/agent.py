"""Flags serverless functions whose average cold-start latency eats most of their configured timeout budget, risking spurious timeout failures."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    cold_start = function.get("avg_cold_start_ms", 0)
    timeout = function.get("timeout_ms", 0)
    if timeout and cold_start > timeout * 0.8:
        findings.append({"severity": "medium", "issue": f"Average cold start ({cold_start}ms) consumes over 80% of the {timeout}ms timeout budget."})
    return findings
