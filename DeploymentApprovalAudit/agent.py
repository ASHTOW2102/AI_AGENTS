"""Review production deployment approval and separation-of-duty evidence."""
from typing import Any


def audit(deployment: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if deployment.get("production") and not deployment.get("approval_reference"):
        findings.append({"severity": "high", "issue": "Production deployment has no approval reference."})
    if deployment.get("production") and deployment.get("deployer") == deployment.get("approver"):
        findings.append({"severity": "medium", "issue": "Deployer and approver are the same identity."})
    if deployment.get("change_window_required") and not deployment.get("change_window_approved"):
        findings.append({"severity": "medium", "issue": "Required change window has not been approved."})
    if deployment.get("emergency") and not deployment.get("post_deployment_review_due"):
        findings.append({"severity": "low", "issue": "Emergency deployment has no post-deployment review due date."})
    return findings
