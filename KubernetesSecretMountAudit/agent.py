"""Review Kubernetes secret mount scope and exposure metadata."""
from typing import Any


def audit(pod: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pod.get("secret_env_var_count", 0) > 0 and not pod.get("env_secret_use_approved"):
        findings.append({"severity": "medium", "issue": "Secrets are injected as environment variables without approval."})
    if pod.get("mounted_secrets", 0) > pod.get("required_secret_count", 0):
        findings.append({"severity": "high", "issue": "Pod mounts more secrets than its declared requirement."})
    if pod.get("secret_mount_writable"):
        findings.append({"severity": "medium", "issue": "Secret volume is writable by the container."})
    if pod.get("cross_namespace_secret_access"):
        findings.append({"severity": "critical", "issue": "Workload can read secrets across namespace boundaries."})
    return findings
