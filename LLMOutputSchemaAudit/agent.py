"""Review model-output contract validation and recovery handling."""
from typing import Any


def audit(contract: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not contract.get("schema_validation"):
        findings.append({"severity": "high", "issue": "Generated output is not validated against a schema."})
    if contract.get("schema_validation") and not contract.get("invalid_output_handling"):
        findings.append({"severity": "medium", "issue": "No safe recovery path is defined for invalid output."})
    if contract.get("strict_json_expected") and contract.get("freeform_fallback"):
        findings.append({"severity": "medium", "issue": "Free-form fallback can bypass the strict output contract."})
    if contract.get("sensitive_fields") and not contract.get("output_redaction"):
        findings.append({"severity": "high", "issue": "Sensitive generated fields are not redacted before release."})
    return findings
