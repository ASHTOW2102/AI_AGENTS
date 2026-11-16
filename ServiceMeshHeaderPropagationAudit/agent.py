"""Flags services in a mesh that fail to propagate distributed tracing headers to downstream calls, breaking trace continuity."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if service.get("makes_downstream_calls") and not service.get("propagates_trace_headers"):
        findings.append({"severity": "medium", "issue": "Service does not propagate tracing headers to downstream calls."})
    if service.get("propagates_trace_headers") and not service.get("propagation_tested"):
        findings.append({"severity": "low", "issue": "Header propagation exists but has not been verified by a trace continuity test."})
    return findings
