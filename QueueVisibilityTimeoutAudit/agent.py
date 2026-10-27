"""Review queue visibility timeouts against consumer processing duration."""
from typing import Any


def audit(queue: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    visibility = queue.get("visibility_timeout_seconds", 0)
    processing = queue.get("p99_processing_seconds", 0)
    if visibility <= processing:
        findings.append({"severity": "high", "issue": "Visibility timeout is not longer than P99 processing time."})
    if queue.get("visibility_timeout_seconds", 0) > queue.get("max_visibility_timeout_seconds", float("inf")):
        findings.append({"severity": "medium", "issue": "Visibility timeout exceeds the service maximum."})
    if queue.get("inflight_limit", 0) > 0 and queue.get("max_concurrent_handlers", 0) > queue["inflight_limit"]:
        findings.append({"severity": "medium", "issue": "Consumer concurrency exceeds the in-flight message limit."})
    if queue.get("long_processing") and not queue.get("timeout_extension_enabled"):
        findings.append({"severity": "medium", "issue": "Long-running message handling cannot extend visibility."})
    return findings
