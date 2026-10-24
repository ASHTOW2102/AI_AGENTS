"""Review mobile certificate-transparency enforcement and failure handling."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not app.get("ct_enforcement_enabled"):
        findings.append({"severity": "high", "issue": "Certificate-transparency enforcement is disabled."})
    if app.get("ct_enforcement_enabled") and app.get("failure_behavior") == "fail_open":
        findings.append({"severity": "high", "issue": "CT validation failure falls open and permits the connection."})
    if app.get("required_scts", 0) < app.get("minimum_scts", 2):
        findings.append({"severity": "medium", "issue": "Required SCT count is below the configured minimum."})
    if not app.get("ct_policy_tested"):
        findings.append({"severity": "low", "issue": "Certificate-transparency behavior has no recorded test evidence."})
    return findings
