"""Flags short-lived authentication tokens with a replay window too large relative to their validity period."""
from typing import Any


def audit(token: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if token.get("nonce_tracking_enabled") is False and token.get("single_use_intended"):
        findings.append({"severity": "high", "issue": "Single-use token has no nonce tracking to prevent replay."})
    if token.get("replay_window_seconds", 0) > token.get("validity_seconds", 1):
        findings.append({"severity": "medium", "issue": "Replay window is as large as or larger than the token's validity period."})
    return findings
