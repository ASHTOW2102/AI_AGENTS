"""Flags networks carrying latency-sensitive and bulk traffic on the same queue with no QoS prioritization configured."""
from typing import Any


def audit(network: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if network.get("carries_latency_sensitive_traffic") and network.get("carries_bulk_traffic") and not network.get("qos_prioritization_configured"):
        findings.append({"severity": "medium", "issue": "Latency-sensitive and bulk traffic share a queue with no QoS prioritization."})
    if network.get("qos_prioritization_configured") and not network.get("qos_policy_tested_under_load"):
        findings.append({"severity": "low", "issue": "QoS policy exists but has not been tested under real load."})
    return findings
