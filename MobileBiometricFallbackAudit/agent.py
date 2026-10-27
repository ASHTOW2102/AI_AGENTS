"""Review mobile biometric fallback and local authentication safeguards."""
from typing import Any


def audit(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if policy.get("biometrics_enabled") and not policy.get("device_credential_fallback"):
        findings.append({"severity": "medium", "issue": "Biometric failure has no device-credential fallback."})
    if policy.get("fallback_to_app_pin") and not policy.get("app_pin_rate_limited"):
        findings.append({"severity": "high", "issue": "App PIN fallback has no attempt throttling."})
    if policy.get("biometric_unlocks_sensitive_action") and not policy.get("fresh_auth_required"):
        findings.append({"severity": "medium", "issue": "Sensitive action accepts stale biometric authentication."})
    if not policy.get("biometric_data_stays_on_device", True):
        findings.append({"severity": "critical", "issue": "Biometric data is reported as leaving the device."})
    return findings
