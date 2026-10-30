"""Compare secret permissions with workload ownership and intended scope."""
from typing import Any


def audit(secret: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    extra = sorted(set(secret.get("authorized_workloads", [])) - set(secret.get("required_workloads", [])))
    if extra:
        findings.append({"severity": "high", "issue": "Secret is accessible to unnecessary workloads: " + ", ".join(extra)})
    if secret.get("shared_across_environments"):
        findings.append({"severity": "medium", "issue": "Secret is shared across production and non-production environments."})
    if not secret.get("workload_identity_binding"):
        findings.append({"severity": "medium", "issue": "Secret access is not bound to a workload identity."})
    if secret.get("wildcard_access"):
        findings.append({"severity": "critical", "issue": "Wildcard principal can access the secret."})
    return findings
