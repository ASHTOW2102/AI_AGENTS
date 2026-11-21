"""Flags database connection pools with prepared statement caching disabled, forcing a full parse/plan cycle on every query execution."""
from typing import Any


def audit(connection_pool: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not connection_pool.get("prepared_statement_cache_enabled"):
        findings.append({"severity": "medium", "issue": "Prepared statement caching is disabled, forcing re-parsing of every query."})
    if connection_pool.get("prepared_statement_cache_enabled") and connection_pool.get("cache_size", 0) < connection_pool.get("distinct_query_shapes", 0):
        findings.append({"severity": "low", "issue": "Prepared statement cache size is smaller than the number of distinct query shapes, causing cache churn."})
    return findings
