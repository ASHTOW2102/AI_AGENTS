"""Flags serverless functions paying for provisioned concurrency far above their observed peak invocation rate."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if function.get("provisioned_concurrency", 0) > function.get("peak_concurrent_invocations", 0) * function.get("max_acceptable_overprovision_ratio", 1.5):
        findings.append({"severity": "medium", "issue": "Provisioned concurrency far exceeds observed peak usage, wasting cost."})
    if function.get("provisioned_concurrency", 0) > 0 and not function.get("usage_reviewed_recently"):
        findings.append({"severity": "low", "issue": "Provisioned concurrency setting has not been reviewed against recent usage."})
    return findings
