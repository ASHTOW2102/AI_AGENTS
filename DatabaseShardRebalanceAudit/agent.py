"""Checks database shard distribution for hot shards and safe rebalancing throttles."""
from typing import Any


def audit(cluster: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if cluster.get("max_shard_size_ratio", 1.0) > cluster.get("max_allowed_size_ratio", 1.5):
        findings.append({"severity": "high", "issue": "A shard significantly exceeds the average shard size."})
    if cluster.get("rebalance_in_progress") and not cluster.get("rebalance_throttled"):
        findings.append({"severity": "medium", "issue": "Rebalance is running without throttling live traffic impact."})
    if cluster.get("hot_shard_qps_ratio", 1.0) > cluster.get("max_hot_shard_qps_ratio", 3.0):
        findings.append({"severity": "high", "issue": "A shard receives disproportionately high query traffic."})
    return findings
