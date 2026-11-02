"""Checks data-warehouse compute spend against query efficiency and idle-cluster signals."""
from typing import Any


def audit(warehouse: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if warehouse.get("idle_hours_per_day", 0) > warehouse.get("max_idle_hours_per_day", 6) and not warehouse.get("auto_suspend_enabled"):
        findings.append({"severity": "medium", "issue": "Warehouse idles frequently without auto-suspend enabled."})
    if warehouse.get("full_table_scan_query_count", 0) > warehouse.get("max_full_scan_queries", 0):
        findings.append({"severity": "high", "issue": "Full table scans exceed the approved query budget."})
    if warehouse.get("monthly_cost", 0) > warehouse.get("budget_alert_threshold", 0) and not warehouse.get("cost_alert_configured"):
        findings.append({"severity": "medium", "issue": "Spend exceeds the alert threshold with no cost alert configured."})
    return findings
