"""Flags web applications stuck in Content-Security-Policy report-only mode without ever enforcing the policy."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("csp_report_only") and app.get("report_only_days", 0) > app.get("max_acceptable_report_only_days", 30):
        findings.append({"severity": "medium", "issue": "CSP has remained in report-only mode past the acceptable grace period."})
    if not app.get("csp_report_only") and not app.get("csp_enforced"):
        findings.append({"severity": "high", "issue": "No Content-Security-Policy is enforced or reported at all."})
    return findings
