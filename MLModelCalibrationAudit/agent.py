"""Review model confidence calibration and threshold evidence."""
from typing import Any


def audit(report: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not report.get("calibration_metric_available"):
        findings.append({"severity": "medium", "issue": "No model confidence calibration metric is recorded."})
    if report.get("expected_calibration_error", 0) > report.get("max_expected_calibration_error", 0.1):
        findings.append({"severity": "high", "issue": "Expected calibration error exceeds the approved limit."})
    if report.get("decision_threshold") is not None and not report.get("threshold_validated"):
        findings.append({"severity": "medium", "issue": "Decision threshold has not been validated on representative data."})
    if report.get("days_since_calibration_review", 0) > report.get("max_review_age_days", 180):
        findings.append({"severity": "low", "issue": "Calibration review is stale."})
    return findings
