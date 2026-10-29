"""Review refund event processing and settlement reconciliation evidence."""
from typing import Any


def audit(refund: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if refund.get("refund_requested") and not refund.get("provider_status_confirmed"):
        findings.append({"severity": "high", "issue": "Refund request lacks provider status confirmation."})
    if refund.get("provider_refunded_amount", 0) != refund.get("ledger_refunded_amount", 0):
        findings.append({"severity": "critical", "issue": "Provider and internal ledger refund totals differ."})
    if refund.get("partial_refund_supported") and not refund.get("remaining_balance_reconciled"):
        findings.append({"severity": "medium", "issue": "Partial refund has no remaining-balance reconciliation."})
    if refund.get("duplicate_refund_events", 0) > 0 and not refund.get("duplicate_events_deduplicated"):
        findings.append({"severity": "high", "issue": "Duplicate refund events are not deduplicated."})
    return findings
