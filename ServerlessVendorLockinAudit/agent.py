"""Checks serverless services for proprietary dependencies that would block migration to another provider."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if service.get("proprietary_event_format_count", 0) > 0 and not service.get("adapter_layer_present"):
        findings.append({"severity": "medium", "issue": "Business logic is coupled directly to a proprietary event format."})
    if service.get("uses_proprietary_managed_database") and not service.get("data_export_tested"):
        findings.append({"severity": "medium", "issue": "Data export from the proprietary managed database has not been tested."})
    if service.get("single_region_only_service_used") and service.get("multi_region_required"):
        findings.append({"severity": "high", "issue": "A single-region-only managed service is used where multi-region is required."})
    return findings
