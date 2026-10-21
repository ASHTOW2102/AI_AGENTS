"""Check third-party dependency operational readiness and incident contacts."""
from typing import Any


def audit(vendor: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not vendor.get("status_page_url"):
        findings.append({"severity": "low", "issue": "No vendor service-status source is recorded."})
    if not vendor.get("incident_contact"):
        findings.append({"severity": "medium", "issue": "No vendor incident escalation contact is recorded."})
    if vendor.get("criticality") == "high" and not vendor.get("support_sla_hours"):
        findings.append({"severity": "high", "issue": "Critical vendor has no documented support response SLA."})
    if vendor.get("last_continuity_review_days", 0) > vendor.get("max_review_interval_days", 365):
        findings.append({"severity": "medium", "issue": "Vendor continuity review is overdue."})
    return findings
