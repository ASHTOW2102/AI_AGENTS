"""Flags feature flags in a partial rollout with no kill switch, so a mid-rollout regression cannot be stopped without a code deploy."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    rollout = flag.get("rollout_percentage", 0)
    if 0 < rollout < 100 and not flag.get("has_kill_switch"):
        findings.append({"severity": "medium", "issue": f"Flag is at a {rollout}% partial rollout with no kill switch to halt it."})
    return findings
