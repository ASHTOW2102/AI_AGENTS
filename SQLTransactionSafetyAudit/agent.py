"""Review SQL transaction plans for bounded scope and safe retry semantics."""
from typing import Any


def audit(transaction: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if transaction.get("writes_data") and not transaction.get("rollback_defined"):
        findings.append({"severity": "medium", "issue": "Data-writing transaction has no rollback strategy."})
    if transaction.get("retryable") and not transaction.get("idempotent"):
        findings.append({"severity": "high", "issue": "Retryable transaction is not idempotent."})
    if transaction.get("isolation_level") == "read_uncommitted" and transaction.get("financial_data"):
        findings.append({"severity": "high", "issue": "Financial transaction uses read-uncommitted isolation."})
    if transaction.get("expected_lock_seconds", 0) > transaction.get("max_lock_seconds", 0):
        findings.append({"severity": "medium", "issue": "Expected lock duration exceeds the transaction budget."})
    return findings
