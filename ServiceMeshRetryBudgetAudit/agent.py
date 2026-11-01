"""Checks service-mesh retry policies for retry budgets and idempotency safety."""
from typing import Any


def audit(policy: dict[str, Any]):
    findings = []
    if policy.get("retries_enabled") and not policy.get("retry_budget_percent"):
        findings.append({"severity": "medium", "issue": "Retries are enabled without a bounded retry budget."})
    if policy.get("retries_enabled") and policy.get("method") in ("POST", "PATCH", "DELETE") and not policy.get("idempotent_confirmed"):
        findings.append({"severity": "high", "issue": "Retries enabled for a non-idempotent-confirmed mutating method."})
    if policy.get("max_retries", 0) > policy.get("approved_max_retries", 3):
        findings.append({"severity": "low", "issue": "Max retry count exceeds the approved limit."})
    return findings
