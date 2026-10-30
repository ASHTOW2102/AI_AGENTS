"""Review webhook signing-secret rotation and overlap policy."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("signing_enabled") and endpoint.get("secret_age_days", 0) > endpoint.get("max_secret_age_days", 365):
        findings.append({"severity": "high", "issue": "Webhook signing secret exceeds its maximum age."})
    if endpoint.get("rotation_in_progress") and not endpoint.get("old_new_overlap_supported"):
        findings.append({"severity": "medium", "issue": "Secret rotation has no safe old/new key overlap."})
    if endpoint.get("signing_enabled") and not endpoint.get("signature_version_tagged"):
        findings.append({"severity": "low", "issue": "Signature payload does not identify its key version."})
    if not endpoint.get("verification_failure_alert"):
        findings.append({"severity": "medium", "issue": "Signature verification failures are not alerted."})
    return findings
