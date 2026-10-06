from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    item: int
    message: str

@dataclass(frozen=True)
class AuditReport:
    healthy: bool
    items_checked: int
    findings: list[Finding]
    recommendations: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def audit(items: list[dict[str, Any]]) -> AuditReport:
    if not isinstance(items, list) or not items:
        raise ValueError("certificates must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        host = str(item.get("hostname", "")).strip()
        if not host:
            raise ValueError(f"item {index}.hostname is required")
        days = item.get("days_remaining")
        bits = item.get("key_bits")
        names = item.get("names")
        if not isinstance(days, int) or isinstance(days, bool):
            raise ValueError(f"item {index}.days_remaining must be an integer")
        if not isinstance(bits, int) or isinstance(bits, bool) or bits <= 0:
            raise ValueError(f"item {index}.key_bits must be a positive integer")
        if not isinstance(names, list) or not all(isinstance(x, str) for x in names):
            raise ValueError(f"item {index}.names must be a string array")
        if days < 0:
            findings.append(Finding("expired", "critical", index, f"{host} is expired."))
        elif days <= 14:
            findings.append(Finding("expires_soon", "high", index, f"{host} expires within 14 days."))
        if host not in names and not any(name.startswith("*.") and host.endswith(name[1:]) for name in names):
            findings.append(Finding("hostname_mismatch", "critical", index, f"{host} is not covered by certificate names."))
        if bits < 2048:
            findings.append(Finding("weak_key", "high", index, f"{host} uses a key below 2048 bits."))
        if item.get("trusted") is not True:
            findings.append(Finding("untrusted_chain", "critical", index, f"{host} is not marked trusted."))
    codes = {finding.code for finding in findings}
    recommendations = (
        [f"Review and resolve: {', '.join(sorted(codes))}.", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class CertWatchAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
