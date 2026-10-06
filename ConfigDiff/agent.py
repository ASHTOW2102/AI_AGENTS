from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

SECURITY_KEYS = {"debug", "authentication_required", "tls_required", "encryption_enabled"}

@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    key: str
    message: str

@dataclass(frozen=True)
class AuditReport:
    healthy: bool
    findings: list[Finding]
    recommendations: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def audit(payload: dict[str, Any]) -> AuditReport:
    if not isinstance(payload, dict):
        raise ValueError("configuration input must be an object")
    baseline = payload.get("baseline")
    current = payload.get("current")
    if not isinstance(baseline, dict) or not isinstance(current, dict):
        raise ValueError("baseline and current must be objects")
    findings: list[Finding] = []
    for key in sorted(baseline.keys() - current.keys()):
        findings.append(Finding("missing_key", "high", str(key), "Baseline key is missing from current configuration."))
    for key in sorted(current.keys() - baseline.keys()):
        findings.append(Finding("new_key", "medium", str(key), "Current configuration adds a key not present in baseline."))
    for key in sorted(baseline.keys() & current.keys()):
        if baseline[key] != current[key]:
            severity = "high" if str(key).lower() in SECURITY_KEYS else "medium"
            findings.append(Finding("changed_security_control" if severity == "high" else "changed_value", severity, str(key), "Value differs from baseline."))
    if current.get("debug") is True:
        findings.append(Finding("debug_enabled", "critical", "debug", "Debug mode is enabled."))
    codes = {finding.code for finding in findings}
    recommendations = ([f"Review and approve drift types: {', '.join(sorted(codes))}.", "Do not place secret values in audit output."] if findings else ["Current configuration matches the baseline."])
    return AuditReport(not findings, findings, recommendations)

class ConfigDiffAgent:
    def inspect(self, payload: dict[str, Any]) -> AuditReport:
        return audit(payload)
