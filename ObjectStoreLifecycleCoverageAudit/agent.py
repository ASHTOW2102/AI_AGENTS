"""Review object-storage lifecycle rules for retention and cleanup coverage."""
from typing import Any


def audit(bucket: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if bucket.get("noncurrent_versions_exist") and not bucket.get("noncurrent_expiry_days"):
        findings.append({"severity": "medium", "issue": "Noncurrent object versions have no expiry policy."})
    if bucket.get("temporary_prefixes") and not bucket.get("temporary_expiry_days"):
        findings.append({"severity": "medium", "issue": "Temporary object paths have no cleanup lifecycle."})
    if bucket.get("incomplete_multipart_uploads_possible") and not bucket.get("multipart_abort_days"):
        findings.append({"severity": "low", "issue": "Incomplete multipart uploads have no abort rule."})
    if bucket.get("required_archive_transition_days", 0) > 0 and bucket.get("archive_transition_days", 0) > bucket["required_archive_transition_days"]:
        findings.append({"severity": "low", "issue": "Archive transition occurs later than the storage policy target."})
    return findings
