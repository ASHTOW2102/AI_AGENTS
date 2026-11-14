"""Flags cloud functions on rarely-exercised error paths that are untested and likely to fail silently under cold invocation."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if function.get("error_path_invocation_count", 0) == 0 and function.get("has_error_handling_code"):
        findings.append({"severity": "medium", "issue": "Error-handling code path has never been exercised by an invocation."})
    if function.get("error_path_invocation_count", 0) == 0 and not function.get("error_path_unit_tested"):
        findings.append({"severity": "high", "issue": "Untested error path with zero production invocations."})
    return findings
