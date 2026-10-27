"""Review customer-data export controls, scope, and delivery evidence."""
from typing import Any


def audit(export: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not export.get("requester_authorized"):
        findings.append({"severity": "high", "issue": "Customer export requester authorization is not confirmed."})
    if export.get("includes_sensitive_fields") and not export.get("field_minimization_reviewed"):
        findings.append({"severity": "medium", "issue": "Sensitive export fields have not been minimized or reviewed."})
    if not export.get("delivery_channel_encrypted"):
        findings.append({"severity": "high", "issue": "Export delivery channel is not confirmed encrypted."})
    if export.get("temporary_copy_created") and not export.get("temporary_copy_expiry_hours"):
        findings.append({"severity": "medium", "issue": "Temporary export copy has no expiry schedule."})
    return findings
