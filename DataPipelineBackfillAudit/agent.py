"""Review planned data backfills for boundedness, checkpoints, and validation."""
from typing import Any


def audit(backfill: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if backfill.get("estimated_rows", 0) > backfill.get("max_rows_per_run", 0) and not backfill.get("chunked"):
        findings.append({"severity": "high", "issue": "Backfill exceeds run limit and is not chunked."})
    if backfill.get("chunked") and not backfill.get("checkpointing"):
        findings.append({"severity": "medium", "issue": "Chunked backfill has no restart checkpointing."})
    if not backfill.get("idempotent"):
        findings.append({"severity": "high", "issue": "Backfill cannot safely resume without duplicate effects."})
    if not backfill.get("post_run_validation"):
        findings.append({"severity": "medium", "issue": "No post-backfill validation is planned."})
    return findings
