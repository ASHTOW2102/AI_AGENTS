"""Checks serverless function concurrency limits against downstream capacity to avoid overload."""
from typing import Any


def audit(fn: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not fn.get("concurrency_limit_configured"):
        findings.append({"severity": "high", "issue": "Function has no reserved concurrency limit."})
    if fn.get("concurrency_limit_configured") and fn.get("max_concurrency", 0) > fn.get("downstream_safe_capacity", 0):
        findings.append({"severity": "high", "issue": "Configured concurrency can overwhelm downstream capacity."})
    if fn.get("shares_account_concurrency_pool") and not fn.get("reserved_concurrency_set"):
        findings.append({"severity": "medium", "issue": "Function can be starved by other functions sharing the account concurrency pool."})
    return findings
