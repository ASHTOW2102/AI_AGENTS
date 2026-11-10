"""Audits containers for missing or overly permissive seccomp profiles."""
from typing import Any


def audit(container: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if container.get("seccomp_profile") in (None, "unconfined"):
        findings.append({"severity": "high", "issue": "Container runs with no or unconfined seccomp profile."})
    if container.get("seccomp_profile") == "custom" and not container.get("profile_reviewed"):
        findings.append({"severity": "medium", "issue": "Custom seccomp profile has not been security-reviewed."})
    return findings
