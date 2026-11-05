"""Checks feature-flag dependency chains for cycles and safe disable ordering."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flag.get("name") in flag.get("depends_on", []):
        findings.append({"severity": "high", "issue": "Feature flag depends on itself, forming a cycle."})
    disabled_but_required = sorted(d for d in flag.get("depends_on", []) if d in flag.get("disabled_dependencies", []))
    if flag.get("enabled") and disabled_but_required:
        findings.append({"severity": "high", "issue": "Flag is enabled while a required dependency is disabled: " + ", ".join(disabled_but_required)})
    if flag.get("depends_on") and not flag.get("dependency_validated_at_evaluation"):
        findings.append({"severity": "medium", "issue": "Flag dependencies are not validated at evaluation time."})
    return findings
