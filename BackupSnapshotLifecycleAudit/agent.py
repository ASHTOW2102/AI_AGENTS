"""Flags disk snapshots that accumulate indefinitely with no lifecycle policy to expire old ones, inflating storage cost and attack surface."""
from typing import Any


def audit(snapshot: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not snapshot.get("lifecycle_policy_configured"):
        findings.append({"severity": "medium", "issue": "Snapshot has no lifecycle policy to expire old copies."})
    if snapshot.get("age_days", 0) > snapshot.get("retention_policy_days", 90) and snapshot.get("lifecycle_policy_configured") is False:
        findings.append({"severity": "low", "issue": "Snapshot has exceeded the intended retention period with nothing enforcing deletion."})
    return findings
