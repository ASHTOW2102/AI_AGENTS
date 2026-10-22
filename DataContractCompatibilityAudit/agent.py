"""Compare producer and consumer data-contract fields for compatibility."""
from typing import Any


def audit(contract: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    removed = sorted(set(contract.get("consumer_required_fields", [])) - set(contract.get("producer_fields", [])))
    if removed:
        findings.append({"severity": "high", "issue": "Consumer-required fields are absent: " + ", ".join(removed)})
    type_changes = contract.get("incompatible_type_changes", [])
    if type_changes:
        findings.append({"severity": "high", "issue": "Incompatible field type changes: " + ", ".join(sorted(type_changes))})
    if contract.get("breaking_change") and not contract.get("version_bumped"):
        findings.append({"severity": "medium", "issue": "Breaking contract change has no version bump."})
    return findings
