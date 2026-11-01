"""Checks chaos-experiment safety controls, blast-radius limits, and rollback readiness."""
from typing import Any


def audit(experiment: dict[str, Any]):
    findings = []
    if not experiment.get("blast_radius_limited"):
        findings.append({"severity": "high", "issue": "Chaos experiment has no blast-radius limit."})
    if not experiment.get("automatic_abort_configured"):
        findings.append({"severity": "high", "issue": "No automatic abort condition is configured."})
    if experiment.get("production") and not experiment.get("stakeholder_notified"):
        findings.append({"severity": "medium", "issue": "Production experiment did not notify stakeholders."})
    if not experiment.get("rollback_plan"):
        findings.append({"severity": "medium", "issue": "Experiment has no documented rollback plan."})
    return findings
