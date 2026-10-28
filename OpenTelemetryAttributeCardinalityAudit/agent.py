"""Review telemetry dimensions for unbounded metric-cardinality risks."""
from typing import Any


def audit(metrics: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for metric in metrics.get("metrics", []):
        name = metric.get("name", "<unnamed>")
        if metric.get("high_cardinality_attributes"):
            attrs = ", ".join(sorted(metric["high_cardinality_attributes"]))
            findings.append({"severity": "high", "issue": f"Metric {name} uses high-cardinality attributes: {attrs}."})
        if metric.get("estimated_series", 0) > metric.get("max_series", 10000):
            findings.append({"severity": "medium", "issue": f"Metric {name} exceeds its series budget."})
    if not metrics.get("cardinality_alert_configured"):
        findings.append({"severity": "low", "issue": "No cardinality growth alert is configured."})
    return findings
