"""Compare dependency licenses against a project's allowed-license policy."""
from typing import Any


def audit(package: dict[str, Any], allowed_licenses: set[str]) -> list[dict[str, str]]:
    findings = []
    license_id = package.get("license")
    if not license_id:
        findings.append({"severity": "medium", "issue": "Dependency has no identified license."})
    elif license_id not in allowed_licenses:
        findings.append({"severity": "high", "issue": f"License {license_id} is not on the approved list."})
    if package.get("copyleft") and not package.get("copyleft_reviewed"):
        findings.append({"severity": "medium", "issue": "Copyleft obligations have not been reviewed."})
    if package.get("license_file_present") is False:
        findings.append({"severity": "low", "issue": "Package distribution omits its license file."})
    return findings
