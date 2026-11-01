"""Checks ETL batch job scheduling for overlap, dependency ordering, and SLA alignment."""
from typing import Any


def audit(job: dict[str, Any]):
    findings = []
    if job.get("depends_on") and not job.get("dependency_wait_configured"):
        findings.append({"severity": "high", "issue": "Job has upstream dependencies without a wait/check configured."})
    if job.get("expected_duration_minutes", 0) > job.get("schedule_window_minutes", 0):
        findings.append({"severity": "medium", "issue": "Expected runtime exceeds the scheduled window."})
    if job.get("overlaps_with_count", 0) > 0 and not job.get("overlap_reviewed"):
        findings.append({"severity": "medium", "issue": "Job overlaps with another scheduled job without review."})
    return findings
