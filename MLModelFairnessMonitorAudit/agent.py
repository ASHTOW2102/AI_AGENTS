"""Review model fairness monitoring coverage and threshold evidence."""
from typing import Any


def audit(report: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not report.get("protected_group_metrics"):
        findings.append({"severity": "high", "issue": "No protected-group performance metrics are tracked."})
    if report.get("max_group_gap", 0) > report.get("approved_max_group_gap", 0):
        findings.append({"severity": "high", "issue": "Observed group performance gap exceeds policy."})
    if report.get("days_since_last_review", 0) > report.get("max_review_age_days", 90):
        findings.append({"severity": "medium", "issue": "Fairness review is stale."})
    if report.get("low_sample_groups", 0) > 0 and not report.get("small_sample_handling"):
        findings.append({"severity": "medium", "issue": "Low-sample groups lack a documented handling policy."})
    return findings
