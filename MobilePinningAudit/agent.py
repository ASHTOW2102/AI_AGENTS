"""Audit mobile application certificate-pinning configuration."""
from __future__ import annotations

from typing import Any


def audit(config: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not config.get("pinning_enabled"):
        findings.append({"severity": "high", "issue": "Certificate pinning is not enabled."})
    if config.get("pinning_enabled") and not config.get("backup_pins"):
        findings.append({"severity": "medium", "issue": "No backup pins are configured for certificate rotation."})
    if config.get("pin_rotation_days", 0) > 365:
        findings.append({"severity": "medium", "issue": "Pin rotation interval exceeds one year."})
    if config.get("debug_bypass_in_release"):
        findings.append({"severity": "critical", "issue": "Debug pinning bypass is enabled in a release build."})
    return findings
