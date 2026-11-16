"""Flags Kubernetes HorizontalPodAutoscalers with scaling thresholds too tight, causing rapid scale up/down thrashing."""
from typing import Any


def audit(hpa: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if hpa.get("scale_events_per_hour", 0) > hpa.get("max_acceptable_scale_events_per_hour", 10):
        findings.append({"severity": "medium", "issue": "HPA is thrashing with excessive scale events per hour."})
    if not hpa.get("stabilization_window_configured"):
        findings.append({"severity": "low", "issue": "No stabilization window is configured to dampen scale thrashing."})
    return findings
