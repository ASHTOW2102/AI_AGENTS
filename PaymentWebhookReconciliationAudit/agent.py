"""Check payment webhook processing for reconciliation and duplicate safety."""
from typing import Any


def audit(flow: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not flow.get("signature_verified"):
        findings.append({"severity": "critical", "issue": "Payment webhook signature is not verified."})
    if not flow.get("event_id_deduplication"):
        findings.append({"severity": "high", "issue": "Duplicate payment events are not deduplicated."})
    if not flow.get("ledger_reconciliation"):
        findings.append({"severity": "high", "issue": "Webhook outcomes are not reconciled with the payment ledger."})
    if flow.get("failed_event_age_hours", 0) > flow.get("max_unreconciled_age_hours", 24):
        findings.append({"severity": "medium", "issue": "Unreconciled payment event exceeds the handling window."})
    return findings
