"""Flags feature flag experiments with randomization or sample-ratio issues that bias results."""
from typing import Any


def audit(experiment: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    ratio = experiment.get("observed_sample_ratio", 1.0)
    if abs(ratio - experiment.get("expected_sample_ratio", 1.0)) > experiment.get("max_acceptable_srm_deviation", 0.05):
        findings.append({"severity": "high", "issue": "Observed sample ratio deviates from expected, indicating a sample-ratio mismatch."})
    if not experiment.get("randomization_unit_consistent"):
        findings.append({"severity": "medium", "issue": "Randomization unit is inconsistent across experiment exposure and analysis."})
    return findings
