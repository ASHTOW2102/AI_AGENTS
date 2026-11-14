"""Flags database queries on partitioned tables that scan all partitions instead of pruning to relevant ones."""
from typing import Any


def audit(query: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if query.get("partitioned_table") and not query.get("partition_key_in_predicate"):
        findings.append({"severity": "medium", "issue": "Query on partitioned table lacks a predicate on the partition key, forcing a full scan."})
    if query.get("partitions_scanned", 0) > query.get("partitions_expected", 1) * 2:
        findings.append({"severity": "high", "issue": "Query scans far more partitions than expected for its predicate."})
    return findings
