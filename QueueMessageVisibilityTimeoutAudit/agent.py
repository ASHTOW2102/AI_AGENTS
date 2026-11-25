"""Flags message queues whose visibility timeout is shorter than the worker's actual processing time, causing in-flight messages to be redelivered and processed twice."""
from typing import Any


def audit(queue: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    visibility_timeout = queue.get("visibility_timeout_s", 0)
    max_processing_time = queue.get("max_processing_time_s", 0)
    if max_processing_time and visibility_timeout < max_processing_time:
        findings.append({"severity": "high", "issue": f"Visibility timeout ({visibility_timeout}s) is shorter than max processing time ({max_processing_time}s), risking duplicate delivery."})
    return findings
