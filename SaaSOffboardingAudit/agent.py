"""Review SaaS account offboarding for access and data-retention completion."""
from typing import Any


def audit(vendor: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if vendor.get("contract_terminated") and vendor.get("active_accounts", 0) > 0:
        findings.append({"severity": "high", "issue": "Active SaaS accounts remain after contract termination."})
    if vendor.get("contract_terminated") and not vendor.get("credentials_revoked"):
        findings.append({"severity": "critical", "issue": "Integration credentials remain valid after termination."})
    if vendor.get("data_return_required") and not vendor.get("data_return_confirmed"):
        findings.append({"severity": "medium", "issue": "Required data return has no completion confirmation."})
    if vendor.get("data_deletion_required") and not vendor.get("deletion_certificate_received"):
        findings.append({"severity": "medium", "issue": "Vendor data deletion certificate is missing."})
    return findings
