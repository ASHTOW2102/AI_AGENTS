"""Checks database primary-key sequences for exhaustion risk against their data-type range."""
from typing import Any


def audit(sequence: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    used_fraction = sequence.get("current_value", 0) / sequence.get("max_value", 1)
    if used_fraction > sequence.get("warning_fraction", 0.8):
        findings.append({"severity": "high", "issue": "Sequence has consumed most of its available range."})
    if sequence.get("data_type") == "int32" and sequence.get("growth_rate_per_day", 0) > 1_000_000:
        findings.append({"severity": "medium", "issue": "High-growth sequence uses a narrow 32-bit integer type."})
    if used_fraction > sequence.get("warning_fraction", 0.8) and not sequence.get("migration_planned"):
        findings.append({"severity": "high", "issue": "Near-exhausted sequence has no migration plan."})
    return findings
