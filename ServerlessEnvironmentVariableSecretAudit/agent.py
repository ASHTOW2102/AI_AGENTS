"""Flags serverless functions storing secrets as plaintext environment variables instead of a dedicated secrets manager."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    plaintext_secrets = [v for v in function.get("env_var_names", []) if v in function.get("secret_like_names", []) and v not in function.get("encrypted_env_vars", [])]
    if plaintext_secrets:
        findings.append({"severity": "high", "issue": f"Secret-like environment variables stored as plaintext: {plaintext_secrets}"})
    if not function.get("uses_secrets_manager"):
        findings.append({"severity": "medium", "issue": "Function does not use a dedicated secrets manager for any credentials."})
    return findings
