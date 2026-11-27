"""Flags service mesh call chains where a callee's timeout is as long or longer than the caller's, so the callee keeps working on a request the caller already gave up on."""
from typing import Any


def audit(mesh: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    caller_timeout = mesh.get("caller_timeout_ms", 0)
    callee_timeout = mesh.get("callee_timeout_ms", 0)
    if caller_timeout and callee_timeout >= caller_timeout:
        findings.append({"severity": "medium", "issue": f"Callee timeout ({callee_timeout}ms) is not shorter than the caller's timeout ({caller_timeout}ms)."})
    return findings
