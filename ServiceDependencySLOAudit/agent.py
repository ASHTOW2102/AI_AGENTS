"""Review service dependency objectives against the service's own SLO."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for dependency in service.get("dependencies", []):
        name = dependency.get("name", "<unnamed>")
        if dependency.get("availability_slo_percent", 100) < service.get("required_dependency_slo_percent", 0):
            findings.append({"severity": "high", "issue": f"Dependency {name} SLO is below service requirement."})
        if dependency.get("critical") and not dependency.get("fallback_defined"):
            findings.append({"severity": "medium", "issue": f"Critical dependency {name} has no fallback behavior."})
        if dependency.get("timeout_ms", 0) > service.get("max_dependency_timeout_ms", 5000):
            findings.append({"severity": "medium", "issue": f"Dependency {name} timeout exceeds the service budget."})
    return findings
