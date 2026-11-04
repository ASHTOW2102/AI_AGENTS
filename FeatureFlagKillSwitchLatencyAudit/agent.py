"""Checks feature-flag kill-switch propagation latency and confirmation evidence under incident pressure."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flag.get("is_kill_switch") and flag.get("propagation_latency_seconds", 0) > flag.get("max_acceptable_latency_seconds", 30):
        findings.append({"severity": "high", "issue": "Kill switch propagation is slower than acceptable for incident response."})
    if flag.get("is_kill_switch") and not flag.get("last_tested_date"):
        findings.append({"severity": "medium", "issue": "Kill switch has never been test-fired."})
    if flag.get("is_kill_switch") and flag.get("requires_deploy_to_toggle"):
        findings.append({"severity": "high", "issue": "Kill switch requires a deployment to toggle, defeating its purpose."})
    return findings
