"""Review CI workflow metadata for secret exposure and fork safety."""
from typing import Any


def audit(workflow: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if workflow.get("secrets_available_to_untrusted_forks"):
        findings.append({"severity": "critical", "issue": "Secrets are available to untrusted fork workflows."})
    if workflow.get("pull_request_target") and workflow.get("executes_checkout_code"):
        findings.append({"severity": "critical", "issue": "Privileged pull_request_target workflow executes untrusted checkout code."})
    if workflow.get("secrets_logged"):
        findings.append({"severity": "critical", "issue": "Workflow may log secret values."})
    if workflow.get("static_credentials"):
        findings.append({"severity": "high", "issue": "CI uses long-lived static credentials."})
    return findings
