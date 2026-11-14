"""Flags data export operations that leave no audit trail of who exported what and when."""
from typing import Any


def audit(export: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not export.get("audit_log_entry_created"):
        findings.append({"severity": "high", "issue": "Data export created no audit log entry."})
    if export.get("audit_log_entry_created") and not export.get("includes_requesting_identity"):
        findings.append({"severity": "medium", "issue": "Audit log entry does not record the requesting identity."})
    return findings
