"""Review distributed tracing sampling coverage and cost safeguards."""
from typing import Any


def audit(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if policy.get("error_sampling_rate_percent", 0) < policy.get("minimum_error_sampling_rate_percent", 100):
        findings.append({"severity": "high", "issue": "Error traces are sampled below the required minimum."})
    if policy.get("head_sampling_rate_percent", 0) > policy.get("max_head_sampling_rate_percent", 100):
        findings.append({"severity": "medium", "issue": "Head-based sampling exceeds the cost policy."})
    if not policy.get("trace_id_propagation"):
        findings.append({"severity": "medium", "issue": "Trace context is not propagated across service boundaries."})
    if policy.get("sensitive_attributes_allowed"):
        findings.append({"severity": "high", "issue": "Sensitive attributes may be recorded in traces."})
    return findings
