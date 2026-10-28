"""Review scheduled-job overlap, concurrency, and missed-run handling."""
from typing import Any


def audit(job: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if job.get("runtime_p99_minutes", 0) >= job.get("schedule_interval_minutes", 0) and not job.get("overlap_lock"):
        findings.append({"severity": "high", "issue": "Job runtime can overlap the next schedule without a lock."})
    if job.get("singleton_required") and not job.get("distributed_lock"):
        findings.append({"severity": "high", "issue": "Singleton job has no distributed concurrency lock."})
    if not job.get("missed_run_policy"):
        findings.append({"severity": "medium", "issue": "Missed scheduled-run behavior is undefined."})
    if job.get("max_parallel_runs", 0) > job.get("approved_max_parallel_runs", 1):
        findings.append({"severity": "medium", "issue": "Parallel run limit exceeds the approved maximum."})
    return findings
