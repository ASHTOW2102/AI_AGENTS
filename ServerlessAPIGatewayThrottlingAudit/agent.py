"""Flags API Gateway routes in front of serverless functions with no throttling configured, letting a traffic spike trigger runaway concurrent invocations and cost."""
from typing import Any


def audit(route: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not route.get("throttle_rate_configured"):
        findings.append({"severity": "high", "issue": "Route has no throttling configured in front of the serverless function."})
    if route.get("throttle_rate_configured") and route.get("throttle_rate_limit", 0) > route.get("downstream_function_concurrency_limit", 0):
        findings.append({"severity": "medium", "issue": "Throttle rate exceeds the downstream function's concurrency limit."})
    return findings
