"""Checks mobile crash reports for inclusion of personal data before transmission to a vendor."""
from typing import Any


def audit(crash_report: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if crash_report.get("includes_raw_user_input") and not crash_report.get("scrubbed_before_send"):
        findings.append({"severity": "high", "issue": "Crash report includes raw user input without scrubbing."})
    if crash_report.get("includes_device_identifiers") and not crash_report.get("identifier_hashing_applied"):
        findings.append({"severity": "medium", "issue": "Crash report includes raw device identifiers."})
    if crash_report.get("sent_to_third_party_vendor") and not crash_report.get("vendor_dpa_signed"):
        findings.append({"severity": "high", "issue": "Crash reports go to a vendor without a signed data processing agreement."})
    return findings
