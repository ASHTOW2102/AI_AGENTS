"""Checks GraphQL persisted-query allowlisting and rejection of unregistered ad-hoc queries."""
from typing import Any


def audit(query: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if query.get("production") and query.get("allows_arbitrary_queries"):
        findings.append({"severity": "high", "issue": "Production endpoint accepts arbitrary unregistered queries."})
    if query.get("persisted_query_required") and not query.get("hash_verified_server_side"):
        findings.append({"severity": "high", "issue": "Persisted query hash is not verified server-side."})
    if query.get("introspection_enabled") and query.get("production"):
        findings.append({"severity": "medium", "issue": "GraphQL introspection is enabled in production."})
    return findings
