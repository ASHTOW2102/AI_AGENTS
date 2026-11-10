"""Flags serverless functions whose cold-start latency exceeds the budget set for their invocation path."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if function.get("cold_start_ms", 0) > function.get("max_acceptable_cold_start_ms", 1000):
        findings.append({"severity": "medium", "issue": "Cold start latency exceeds the acceptable budget."})
    if function.get("on_critical_path") and not function.get("provisioned_concurrency_enabled"):
        findings.append({"severity": "high", "issue": "Critical-path function has no provisioned concurrency to avoid cold starts."})
    return findings
