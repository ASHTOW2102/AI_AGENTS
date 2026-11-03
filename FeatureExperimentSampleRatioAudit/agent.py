"""Checks A/B experiment sample-ratio mismatch between control and treatment groups."""
from typing import Any


def audit(experiment: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    ratio = experiment.get("observed_ratio", 1.0)
    expected = experiment.get("expected_ratio", 1.0)
    if expected and abs(ratio - expected) / expected > experiment.get("max_deviation_fraction", 0.05):
        findings.append({"severity": "high", "issue": "Observed sample ratio deviates significantly from the expected allocation."})
    if experiment.get("sample_size", 0) < experiment.get("min_sample_size_for_power", 0):
        findings.append({"severity": "medium", "issue": "Sample size is below the level needed for statistical power."})
    if experiment.get("running_days", 0) > experiment.get("max_planned_days", 30) and not experiment.get("extension_approved"):
        findings.append({"severity": "low", "issue": "Experiment runs past its planned duration without approval."})
    return findings
