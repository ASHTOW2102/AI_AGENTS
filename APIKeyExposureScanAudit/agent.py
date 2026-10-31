"""Review repository scan summaries for exposed API keys and remediation."""
from typing import Any


def audit(scan: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if scan.get("active_secret_findings", 0) > 0:
        findings.append({"severity": "critical", "issue": "Active API-key findings remain in scanned source."})
    if scan.get("scan_completed") is False:
        findings.append({"severity": "high", "issue": "Secret scan did not complete successfully."})
    if not scan.get("history_scan_enabled"):
        findings.append({"severity": "medium", "issue": "Historical repository content is not included in scanning."})
    if scan.get("exceptions_unreviewed", 0) > 0:
        findings.append({"severity": "low", "issue": "Secret scan exceptions have not been reviewed."})
    return findings
