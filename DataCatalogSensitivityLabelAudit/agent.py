"""Flags data catalog assets containing known-sensitive column patterns that have no sensitivity label applied, so downstream tools can't enforce handling policy."""
from typing import Any


def audit(asset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if asset.get("contains_sensitive_pattern") and not asset.get("sensitivity_label_applied"):
        findings.append({"severity": "high", "issue": "Asset contains a sensitive data pattern but has no sensitivity label applied."})
    if asset.get("sensitivity_label_applied") and asset.get("label_last_reviewed_days_ago", 0) > asset.get("max_acceptable_review_interval_days", 365):
        findings.append({"severity": "low", "issue": "Sensitivity label has not been reviewed within the acceptable interval."})
    return findings
