"""Review distributed data partition size and workload skew."""
from typing import Any


def audit(profile: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    sizes = profile.get("partition_sizes", [])
    if sizes and min(sizes) > 0 and max(sizes) / min(sizes) > profile.get("max_size_ratio", 3):
        findings.append({"severity": "medium", "issue": "Partition sizes exceed the allowed skew ratio."})
    loads = profile.get("partition_loads", [])
    if loads and min(loads) > 0 and max(loads) / min(loads) > profile.get("max_load_ratio", 3):
        findings.append({"severity": "high", "issue": "Partition workload is concentrated on a small subset."})
    if profile.get("empty_partitions", 0) > 0:
        findings.append({"severity": "low", "issue": "One or more configured partitions contain no data."})
    return findings
