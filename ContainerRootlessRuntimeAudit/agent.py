"""Checks that containers run under a rootless runtime configuration instead of root-mapped namespaces."""
from typing import Any


def audit(container: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if container.get("runs_as_root") and not container.get("rootless_runtime_enabled"):
        findings.append({"severity": "high", "issue": "Container runs as root without a rootless runtime."})
    if container.get("rootless_runtime_enabled") and container.get("uid_mapping") == "direct":
        findings.append({"severity": "medium", "issue": "Rootless runtime uses direct UID mapping instead of a user namespace offset."})
    return findings
