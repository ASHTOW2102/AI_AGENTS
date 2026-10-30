"""Review service catalog ownership and operational-contact freshness."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not service.get("technical_owner"):
        findings.append({"severity": "high", "issue": "Service has no technical owner."})
    if not service.get("business_owner"):
        findings.append({"severity": "medium", "issue": "Service has no business owner."})
    if service.get("owner_review_age_days", 0) > service.get("max_owner_review_age_days", 365):
        findings.append({"severity": "low", "issue": "Service ownership record has not been reviewed recently."})
    if service.get("on_call_required") and not service.get("on_call_route_verified"):
        findings.append({"severity": "high", "issue": "Required on-call route has not been verified."})
    return findings
