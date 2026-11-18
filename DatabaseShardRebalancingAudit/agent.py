"""Flags sharded database clusters with significant data skew across shards and no automated rebalancing in place."""
from typing import Any


def audit(cluster: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    max_shard = max(cluster.get("shard_sizes_gb", [0]))
    min_shard = min(cluster.get("shard_sizes_gb", [0]))
    if min_shard > 0 and (max_shard / min_shard) > cluster.get("max_acceptable_skew_ratio", 2.0):
        findings.append({"severity": "medium", "issue": "Shard size skew exceeds the acceptable ratio between largest and smallest shard."})
    if not cluster.get("automated_rebalancing_enabled"):
        findings.append({"severity": "low", "issue": "No automated shard rebalancing is configured."})
    return findings
