"""Review runtime API rate-limit observations and tenant isolation."""
from __future__ import annotations

from typing import Any


def audit(metrics: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if metrics.get("throttled_requests", 0) > 0 and not metrics.get("throttle_alert_configured"):
        findings.append({"severity": "medium", "issue": "Throttling is occurring without an alert."})
    if metrics.get("throttle_5xx_rate", 0) > metrics.get("max_throttle_5xx_rate", 0):
        findings.append({"severity": "high", "issue": "Throttling is associated with excessive server errors."})
    if metrics.get("limit_saturation_percent", 0) >= 90:
        findings.append({"severity": "medium", "issue": "Rate-limit capacity is at least 90% saturated."})
    if not metrics.get("per_tenant_limits"):
        findings.append({"severity": "high", "issue": "Rate limits are not isolated per tenant."})
    return findings
