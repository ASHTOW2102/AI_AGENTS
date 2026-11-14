"""Flags feature flag targeting rules that expose internal segment names or unreleased feature identifiers to client bundles."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flag.get("targeting_rules_shipped_to_client") and flag.get("contains_internal_segment_names"):
        findings.append({"severity": "medium", "issue": "Targeting rules shipped to the client expose internal segment names."})
    if flag.get("flag_name_reveals_unreleased_feature") and flag.get("shipped_to_client"):
        findings.append({"severity": "high", "issue": "Flag name reveals an unreleased feature and is shipped to the client."})
    return findings
