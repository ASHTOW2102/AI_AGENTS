"""Review Kubernetes ingress TLS and redirect policy metadata."""
from typing import Any


def audit(ingress: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if ingress.get("public") and not ingress.get("tls_secret"):
        findings.append({"severity": "high", "issue": "Public ingress has no TLS certificate configured."})
    if ingress.get("tls_secret") and not ingress.get("https_redirect"):
        findings.append({"severity": "medium", "issue": "HTTPS traffic is not enforced with a redirect."})
    if ingress.get("hosts") and not set(ingress["hosts"]).issubset(set(ingress.get("certificate_hosts", []))):
        findings.append({"severity": "high", "issue": "Certificate does not cover every ingress hostname."})
    if ingress.get("tls_min_version", "TLS1.2") < "TLS1.2":
        findings.append({"severity": "high", "issue": "Ingress permits TLS versions older than 1.2."})
    return findings
