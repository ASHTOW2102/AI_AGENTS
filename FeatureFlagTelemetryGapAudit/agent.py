"""Flags feature flags with no telemetry tied to their variants, making it impossible to tell whether a rollout is actually having the intended effect."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not flag.get("variant_exposure_logged"):
        findings.append({"severity": "medium", "issue": "Flag variant exposure is not logged, so rollout impact can't be measured."})
    if flag.get("variant_exposure_logged") and not flag.get("linked_to_success_metric"):
        findings.append({"severity": "low", "issue": "Exposure is logged but not linked to any success metric."})
    return findings
