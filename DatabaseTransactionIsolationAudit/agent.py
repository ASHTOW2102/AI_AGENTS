"""Flags transactions that require serializable isolation for correctness but run at a weaker configured isolation level."""
from typing import Any


def audit(transaction: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if transaction.get("requires_serializable") and transaction.get("isolation_level") != "SERIALIZABLE":
        findings.append({"severity": "high", "issue": f"Transaction requires serializable isolation but runs at '{transaction.get('isolation_level')}'."})
    return findings
