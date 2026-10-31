"""Review analytics query plans for partition pruning and scan bounds."""
from typing import Any


def audit(query: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if query.get("partitioned_table") and not query.get("partition_filter_present"):
        findings.append({"severity": "medium", "issue": "Query omits a filter on the partition key."})
    if query.get("estimated_scanned_bytes", 0) > query.get("max_scanned_bytes", 0):
        findings.append({"severity": "high", "issue": "Estimated data scan exceeds the query budget."})
    if query.get("full_scan_expected") and not query.get("scan_approval_reference"):
        findings.append({"severity": "low", "issue": "Expected full scan has no approval reference."})
    if query.get("partition_count_scanned", 0) > query.get("max_partitions_scanned", 0):
        findings.append({"severity": "medium", "issue": "Query scans more partitions than the configured maximum."})
    return findings
