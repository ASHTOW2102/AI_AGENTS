"""Review serverless cold-start latency and mitigation coverage."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if function.get("p95_cold_start_ms", 0) > function.get("max_p95_cold_start_ms", 1000):
        findings.append({"severity": "high", "issue": "P95 cold-start latency exceeds the target."})
    if function.get("initialization_error_rate_percent", 0) > function.get("max_initialization_error_rate_percent", 1):
        findings.append({"severity": "high", "issue": "Initialization error rate exceeds the target."})
    if function.get("critical_path") and not function.get("provisioned_capacity"):
        findings.append({"severity": "medium", "issue": "Critical-path function has no reserved warm capacity."})
    if not function.get("cold_start_dashboard"):
        findings.append({"severity": "low", "issue": "Cold-start latency is not represented on a dashboard."})
    return findings
