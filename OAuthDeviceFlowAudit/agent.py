"""Review OAuth device authorization flow rate limits and user-code policy."""
from typing import Any


def audit(flow: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flow.get("device_flow_enabled") and not flow.get("user_code_entropy_adequate"):
        findings.append({"severity": "high", "issue": "Device authorization user code has insufficient entropy."})
    if flow.get("device_flow_enabled") and not flow.get("polling_rate_limited"):
        findings.append({"severity": "medium", "issue": "Device authorization polling is not rate limited."})
    if flow.get("device_code_ttl_seconds", 0) > flow.get("max_device_code_ttl_seconds", 1800):
        findings.append({"severity": "medium", "issue": "Device code remains valid longer than policy."})
    if not flow.get("user_consent_displayed") and flow.get("device_flow_enabled"):
        findings.append({"severity": "high", "issue": "Authorization server does not clearly display user consent context."})
    return findings
