"""Checks application configuration sources for database connection strings exposed in plaintext."""
from typing import Any


def audit(config: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if config.get("connection_string_in_source_control"):
        findings.append({"severity": "critical", "issue": "Database connection string is committed to source control."})
    if config.get("connection_string_in_logs"):
        findings.append({"severity": "high", "issue": "Connection string appears in application logs."})
    if config.get("stored_in_secret_manager") is False and config.get("contains_credentials"):
        findings.append({"severity": "high", "issue": "Connection string with embedded credentials is not stored in a secret manager."})
    return findings
