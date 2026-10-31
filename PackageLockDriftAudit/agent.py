"""Compare installed package versions with lockfile and policy constraints."""
from typing import Any


def audit(report: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for package in report.get("packages", []):
        name = package.get("name", "<unnamed>")
        if package.get("installed_version") != package.get("locked_version"):
            findings.append({"severity": "high", "issue": f"{name} installed version differs from lockfile."})
        if package.get("floating_constraint"):
            findings.append({"severity": "medium", "issue": f"{name} uses a floating version constraint."})
    if report.get("lockfile_out_of_date"):
        findings.append({"severity": "medium", "issue": "Lockfile does not match current dependency declarations."})
    return findings
