"""Review Content Security Policy directives for browser-side exposure."""
from typing import Any


def audit(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    directives = policy.get("directives", {})
    if "default-src" not in directives:
        findings.append({"severity": "medium", "issue": "CSP has no default-src fallback directive."})
    if policy.get("production") and policy.get("unsafe_inline"):
        findings.append({"severity": "high", "issue": "Production CSP permits unsafe-inline scripts or styles."})
    if policy.get("production") and policy.get("wildcard_sources"):
        findings.append({"severity": "high", "issue": "Production CSP contains wildcard sources."})
    if not policy.get("reporting_configured"):
        findings.append({"severity": "low", "issue": "CSP violation reporting is not configured."})
    return findings
