"""Review container runtime profiles for seccomp and privilege restrictions."""
from typing import Any


def audit(runtime: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if runtime.get("seccomp_profile", "") in {"", "unconfined"}:
        findings.append({"severity": "high", "issue": "Container has no restrictive seccomp profile."})
    if runtime.get("privilege_escalation_allowed"):
        findings.append({"severity": "high", "issue": "Container permits privilege escalation."})
    if runtime.get("root_user") and not runtime.get("root_required_exception"):
        findings.append({"severity": "medium", "issue": "Container runs as root without an approved exception."})
    if runtime.get("unmasked_proc"):
        findings.append({"severity": "medium", "issue": "Sensitive /proc paths are not masked."})
    return findings
