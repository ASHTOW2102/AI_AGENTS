"""Checks git history scan results for leaked secrets and remediation evidence."""
from typing import Any


def audit(scan: dict[str, Any]):
    findings = []
    if scan.get("secrets_found", 0) > 0 and not scan.get("secrets_rotated"):
        findings.append({"severity": "critical", "issue": "Leaked secrets found in history were not rotated."})
    if scan.get("secrets_found", 0) > 0 and not scan.get("history_rewritten") and not scan.get("secrets_rotated"):
        findings.append({"severity": "high", "issue": "Leaked secret remains reachable in git history."})
    if scan.get("scan_age_days", 0) > scan.get("max_scan_age_days", 30):
        findings.append({"severity": "low", "issue": "Secret-history scan is stale."})
    return findings
