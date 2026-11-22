"""Flags GraphQL endpoints that accept arbitrarily deep or recursive queries without a configured maximum query depth, enabling resource-exhaustion attacks."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    max_depth = endpoint.get("max_query_depth")
    allows_recursive = endpoint.get("allows_recursive_fragments", False)

    if not max_depth:
        findings.append({"severity": "high", "issue": "GraphQL endpoint has no maximum query depth configured, allowing arbitrarily deep nested queries to exhaust server resources."})
    elif max_depth > 15:
        findings.append({"severity": "medium", "issue": f"Maximum query depth of {max_depth} is unusually high and may still permit expensive nested queries."})

    if allows_recursive and not endpoint.get("fragment_cycle_detection"):
        findings.append({"severity": "high", "issue": "Recursive fragments are allowed with no cycle detection, enabling infinite query expansion."})
    return findings
