"""Flags workloads with unrestricted outbound network access instead of an explicit egress allowlist."""
from typing import Any


def audit(workload: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if workload.get("egress_policy") == "allow_all":
        findings.append({"severity": "high", "issue": "Workload has unrestricted outbound egress."})
    if workload.get("egress_policy") == "allowlist" and not workload.get("allowlist_reviewed"):
        findings.append({"severity": "medium", "issue": "Egress allowlist exists but has not been security-reviewed."})
    return findings
