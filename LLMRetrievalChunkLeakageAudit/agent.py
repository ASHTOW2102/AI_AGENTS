"""Flags RAG pipelines whose retrieval step can return document chunks the requesting user is not authorized to view."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pipeline.get("retrieval_spans_multiple_permission_levels") and not pipeline.get("retrieval_filters_by_requester_permissions"):
        findings.append({"severity": "high", "issue": "Retrieval store spans multiple permission levels but does not filter by the requester's permissions."})
    if pipeline.get("retrieval_filters_by_requester_permissions") and not pipeline.get("filter_tested_for_bypass"):
        findings.append({"severity": "medium", "issue": "Permission filter exists but has not been tested for bypass via crafted queries."})
    return findings
