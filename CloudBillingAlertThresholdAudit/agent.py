"""Flags cloud accounts with no budget alert configured, so a cost spike (runaway resource, abuse, misconfiguration) goes unnoticed until the invoice arrives."""
from typing import Any


def audit(billing: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not billing.get("has_budget_alert"):
        findings.append({"severity": "medium", "issue": "No budget alert is configured on this account."})
    return findings
