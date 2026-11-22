"""Flags critical features gated behind a feature flag with no remotely-toggleable kill switch, forcing a full deploy to disable a feature that is misbehaving in production."""
from typing import Any


def audit(feature: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    is_critical = feature.get("is_critical_path", False)
    has_remote_kill_switch = feature.get("has_remote_kill_switch", False)

    if is_critical and not has_remote_kill_switch:
        findings.append({"severity": "high", "issue": "Critical-path feature has no remotely-toggleable kill switch, so disabling it during an incident requires a full redeploy."})
    if feature.get("kill_switch_requires_restart"):
        findings.append({"severity": "medium", "issue": "Kill switch exists but requires a process restart to take effect, slowing incident response."})
    return findings
