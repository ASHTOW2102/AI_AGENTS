"""Review database index inventories for redundancy and unindexed query paths."""
from typing import Any


def audit(report: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for index in report.get("indexes", []):
        name = index.get("name", "<unnamed>")
        if index.get("unused_days", 0) > report.get("unused_warning_days", 90) and not index.get("constraint_backing"):
            findings.append({"severity": "low", "issue": f"Index {name} has been unused beyond the review window."})
        if index.get("duplicate_of"):
            findings.append({"severity": "medium", "issue": f"Index {name} duplicates {index['duplicate_of']}."})
    if report.get("critical_queries_without_index", 0) > 0:
        findings.append({"severity": "high", "issue": "Critical query plans include unindexed access paths."})
    return findings
