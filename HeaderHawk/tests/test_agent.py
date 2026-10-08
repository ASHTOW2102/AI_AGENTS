import pytest
from agent import HeaderHawkAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"url":"https://example.com","status":200,"headers":{"strict-transport-security":"max-age=31536000","content-security-policy":"default-src 'self'","x-content-type-options":"nosniff","referrer-policy":"strict-origin"}}]).healthy

def test_risky_input_is_detected():
    assert {"missing_hsts","missing_csp","missing_nosniff","missing_referrer_policy","wildcard_cors"} <= codes(audit([{"url":"https://example.com","status":200,"headers":{"access-control-allow-origin":"*"}}]))

def test_agent_delegates_to_audit():
    assert HeaderHawkAgent().inspect([{"url":"https://example.com","status":200,"headers":{"strict-transport-security":"max-age=31536000","content-security-policy":"default-src 'self'","x-content-type-options":"nosniff","referrer-policy":"strict-origin"}}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
