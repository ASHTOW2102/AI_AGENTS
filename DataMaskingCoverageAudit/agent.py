"""Checks non-production environments for sensitive-field masking coverage on copied production data."""
from typing import Any


def audit(environment: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    unmasked = sorted(set(environment.get("sensitive_fields", [])) - set(environment.get("masked_fields", [])))
    if unmasked and environment.get("tier") != "production":
        findings.append({"severity": "high", "issue": "Non-production environment exposes unmasked sensitive fields: " + ", ".join(unmasked)})
    if environment.get("masking_applied") and environment.get("masking_reversible"):
        findings.append({"severity": "medium", "issue": "Masking transformation is reversible."})
    if environment.get("refreshed_from_production") and not environment.get("masking_applied_on_refresh"):
        findings.append({"severity": "high", "issue": "Data refresh from production does not reapply masking."})
    return findings
