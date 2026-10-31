"""Review data-subject request completion timing and escalation coverage."""
from typing import Any


def audit(request: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if request.get("age_days", 0) > request.get("completion_sla_days", 30) and not request.get("extension_approved"):
        findings.append({"severity": "high", "issue": "Request exceeds completion SLA without an approved extension."})
    if request.get("days_until_due", 99999) <= request.get("warning_window_days", 7) and not request.get("owner_assigned"):
        findings.append({"severity": "high", "issue": "Request is approaching its due date without an assigned owner."})
    if request.get("identity_verification_required") and not request.get("identity_verified"):
        findings.append({"severity": "medium", "issue": "Required requester identity verification is incomplete."})
    if request.get("closed") and not request.get("completion_evidence_reference"):
        findings.append({"severity": "medium", "issue": "Closed request has no completion evidence reference."})
    return findings
