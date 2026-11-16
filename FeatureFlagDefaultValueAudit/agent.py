"""Flags feature flags whose default/fallback value when the flag service is unreachable is riskier than the safe default."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flag.get("fallback_value") != flag.get("safe_default_value"):
        findings.append({"severity": "high", "issue": "Fallback value on service outage differs from the designated safe default."})
    if not flag.get("fallback_behavior_tested"):
        findings.append({"severity": "medium", "issue": "Fallback behavior has never been tested under a simulated outage."})
    return findings
