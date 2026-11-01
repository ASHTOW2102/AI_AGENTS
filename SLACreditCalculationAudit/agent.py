"""Checks SLA breach detection and customer-credit calculation accuracy and evidence."""
from typing import Any


def audit(period: dict[str, Any]):
    findings = []
    if period.get("uptime_percent", 100) < period.get("sla_target_percent", 99.9) and not period.get("credit_issued"):
        findings.append({"severity": "high", "issue": "SLA breach occurred but no credit was issued."})
    if period.get("credit_issued") and not period.get("credit_calculation_evidence"):
        findings.append({"severity": "medium", "issue": "Issued credit has no calculation evidence on file."})
    if period.get("credit_amount", 0) < period.get("contractual_minimum_credit", 0):
        findings.append({"severity": "high", "issue": "Credit amount is below the contractual minimum."})
    return findings
