"""Flags search indexes that mix documents from multiple tenants or permission levels without per-document access filtering at query time."""
from typing import Any


def audit(index: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if index.get("multi_tenant_documents") and not index.get("document_level_access_filter_enabled"):
        findings.append({"severity": "high", "issue": "Multi-tenant index has no document-level access filtering at query time."})
    if index.get("document_level_access_filter_enabled") and not index.get("filter_bypass_tested"):
        findings.append({"severity": "medium", "issue": "Access filter exists but has not been tested for bypass via query crafting."})
    return findings
