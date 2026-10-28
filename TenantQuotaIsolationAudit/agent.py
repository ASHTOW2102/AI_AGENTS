"""Review tenant quota enforcement and cross-tenant resource isolation."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if service.get("multi_tenant") and not service.get("quota_enforced_per_tenant"):
        findings.append({"severity": "high", "issue": "Resource quota is not enforced per tenant."})
    if service.get("tenant_override_count", 0) > 0 and not service.get("override_expiry_enforced"):
        findings.append({"severity": "medium", "issue": "Tenant quota overrides do not expire automatically."})
    if service.get("quota_usage_check") and not service.get("tenant_id_bound_to_identity"):
        findings.append({"severity": "critical", "issue": "Quota checks are not bound to the authenticated tenant identity."})
    if not service.get("quota_exhaustion_alert"):
        findings.append({"severity": "low", "issue": "No alert is configured for tenant quota exhaustion."})
    return findings
