"""Checks serverless function timeout budgets against downstream call latency totals."""
from typing import Any


def audit(fn: dict[str, Any]):
    findings = []
    if fn.get("sum_downstream_timeout_ms", 0) > fn.get("function_timeout_ms", 0):
        findings.append({"severity": "high", "issue": "Downstream timeouts can exceed the function timeout budget."})
    if fn.get("function_timeout_ms", 0) > fn.get("max_approved_timeout_ms", 0):
        findings.append({"severity": "medium", "issue": "Function timeout exceeds the approved maximum."})
    if fn.get("cold_start_ms", 0) > fn.get("function_timeout_ms", 1) * 0.5:
        findings.append({"severity": "low", "issue": "Cold start consumes a large share of the timeout budget."})
    return findings
