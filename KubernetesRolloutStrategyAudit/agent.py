"""Review Kubernetes rollout strategy for availability and rollback limits."""
from typing import Any


def audit(deployment: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if deployment.get("replicas", 0) > 1 and deployment.get("max_unavailable", 0) >= deployment["replicas"]:
        findings.append({"severity": "high", "issue": "Rollout can make every replica unavailable at once."})
    if deployment.get("max_surge", 0) < 0:
        findings.append({"severity": "medium", "issue": "Rollout maxSurge must not be negative."})
    if deployment.get("progress_deadline_seconds", 0) <= 0:
        findings.append({"severity": "medium", "issue": "Deployment has no positive progress deadline."})
    if deployment.get("automatic_rollback_expected") and not deployment.get("rollback_controller_enabled"):
        findings.append({"severity": "high", "issue": "Automatic rollback is expected but no rollback controller is enabled."})
    return findings
