"""Flags datasets requiring cross-table join consistency whose masking is non-deterministic, breaking joins between separately masked copies of the same value."""
from typing import Any


def audit(dataset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if dataset.get("requires_join_consistency") and not dataset.get("masking_is_deterministic"):
        findings.append({"severity": "medium", "issue": "Join-dependent dataset uses non-deterministic masking, breaking cross-table joins."})
    return findings
