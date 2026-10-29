"""Review cloud egress controls for DNS, destination, and logging coverage."""
from typing import Any


def audit(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if policy.get("unrestricted_egress_rules", 0) > 0:
        findings.append({"severity": "high", "issue": "One or more unrestricted outbound rules are present."})
    if policy.get("dns_egress_required") and not policy.get("approved_dns_resolver_only"):
        findings.append({"severity": "medium", "issue": "DNS egress is not restricted to approved resolvers."})
    if policy.get("egress_restrictions_enabled") and not policy.get("egress_flow_logging"):
        findings.append({"severity": "low", "issue": "Restricted egress has no flow logging for investigation."})
    if policy.get("sensitive_workload") and policy.get("public_internet_egress") and not policy.get("exception_approved"):
        findings.append({"severity": "high", "issue": "Sensitive workload has unapproved public internet egress."})
    return findings
