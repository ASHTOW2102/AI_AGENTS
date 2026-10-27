"""Review multi-factor authentication recovery and fallback protections."""
from typing import Any


def audit(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if policy.get("mfa_required") and not policy.get("recovery_flow_tested"):
        findings.append({"severity": "medium", "issue": "MFA recovery flow has no recorded test evidence."})
    if policy.get("support_can_disable_mfa") and not policy.get("identity_verification_required"):
        findings.append({"severity": "critical", "issue": "Support can disable MFA without verified user identity."})
    if policy.get("backup_codes_enabled") and not policy.get("backup_codes_one_time"):
        findings.append({"severity": "high", "issue": "Backup codes are not restricted to one-time use."})
    if policy.get("recovery_bypasses_mfa") and not policy.get("recovery_step_up_auth"):
        findings.append({"severity": "high", "issue": "Account recovery bypasses MFA without an alternate step-up check."})
    return findings
