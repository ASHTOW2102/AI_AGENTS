"""Review SAML assertion validation and replay protections."""
from typing import Any


def audit(sp: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not sp.get("signature_validation"):
        findings.append({"severity": "critical", "issue": "SAML assertion signature is not validated."})
    if not sp.get("audience_validation"):
        findings.append({"severity": "high", "issue": "SAML audience restriction is not validated."})
    if not sp.get("recipient_validation"):
        findings.append({"severity": "high", "issue": "Assertion recipient is not validated."})
    if not sp.get("assertion_replay_cache"):
        findings.append({"severity": "high", "issue": "Previously consumed SAML assertions can be replayed."})
    return findings
