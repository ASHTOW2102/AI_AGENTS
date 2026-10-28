"""Review rate-limit partitioning for tenant fairness and noisy-neighbor risks."""
from typing import Any


def audit(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if policy.get("multi_tenant") and not policy.get("per_tenant_partitioning"):
        findings.append({"severity": "high", "issue": "Tenants share a global limit with no per-tenant partition."})
    if policy.get("tenant_limit", 0) > policy.get("approved_tenant_limit", 0):
        findings.append({"severity": "medium", "issue": "Tenant limit exceeds the approved quota."})
    if policy.get("priority_tiers") and not policy.get("lower_tier_capacity_reserved"):
        findings.append({"severity": "medium", "issue": "Priority tiers have no reserved capacity for lower tiers."})
    if not policy.get("limit_rejection_metric"):
        findings.append({"severity": "low", "issue": "Rate-limit rejections are not measured."})
    return findings
