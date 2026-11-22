"""Flags edge/serverless functions with heavy initialization work on every cold start (large dependency graphs, synchronous remote config fetches) with no warm-pool or provisioned-concurrency mitigation."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    cold_start_ms = function.get("p99_cold_start_ms", 0)
    has_mitigation = function.get("uses_provisioned_concurrency") or function.get("uses_warm_pool")
    fetches_config_sync = function.get("fetches_remote_config_synchronously_on_init", False)

    if cold_start_ms > 1000 and not has_mitigation:
        findings.append({"severity": "medium", "issue": f"p99 cold start is {cold_start_ms}ms with no provisioned concurrency or warm pool, exposing latency-sensitive callers to tail latency."})
    if fetches_config_sync:
        findings.append({"severity": "medium", "issue": "Function fetches remote configuration synchronously during cold start init, adding network latency and a new failure mode to every cold invocation."})
    return findings
