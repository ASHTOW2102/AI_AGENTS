"""Review DNSSEC deployment and signing-key rollover metadata."""
from typing import Any


def audit(zone: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not zone.get("dnssec_enabled"):
        findings.append({"severity": "high", "issue": "DNSSEC signing is not enabled for the zone."})
    if zone.get("dnssec_enabled") and not zone.get("ds_published"):
        findings.append({"severity": "high", "issue": "Parent-zone DS record is not confirmed."})
    if zone.get("key_age_days", 0) > zone.get("max_key_age_days", 365):
        findings.append({"severity": "medium", "issue": "Signing key exceeds its maximum planned age."})
    if zone.get("rollover_in_progress") and not zone.get("overlapping_keys"):
        findings.append({"severity": "high", "issue": "Key rollover has no overlap period for safe propagation."})
    return findings
