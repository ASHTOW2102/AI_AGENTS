"""Flags serverless functions whose reserved concurrency exceeds a downstream dependency's connection limit, risking connection exhaustion under load."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    reserved = function.get("reserved_concurrency", 0)
    downstream_limit = function.get("downstream_connection_limit", 0)
    if downstream_limit and reserved > downstream_limit:
        findings.append({"severity": "high", "issue": f"Reserved concurrency ({reserved}) exceeds downstream connection limit ({downstream_limit})."})
    return findings
