"""Flags API endpoints that interpolate query string parameters directly into backend shell commands or file paths."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("query_param_passed_to_shell") and not endpoint.get("shell_arg_escaping_applied"):
        findings.append({"severity": "high", "issue": "Query parameter is passed to a shell command without escaping."})
    if endpoint.get("query_param_used_as_file_path") and not endpoint.get("path_traversal_sanitized"):
        findings.append({"severity": "high", "issue": "Query parameter is used as a file path without path-traversal sanitization."})
    return findings
