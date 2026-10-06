import pytest
from agent import CookieCheckAgent, audit

def codes(report):
    return {item.code for item in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"session","secure":True,"http_only":True,"same_site":"Lax","max_age_seconds":3600,"domain":"app.example.com"}]).healthy

def test_risky_input_is_detected():
    assert {"missing_secure", "missing_http_only", "weak_same_site", "long_lifetime", "broad_domain"} <= codes(audit([{"name":"session","secure":False,"http_only":False,"same_site":"None","max_age_seconds":99999999,"domain":".example.com"}]))

def test_agent_delegates_to_audit():
    assert CookieCheckAgent().inspect([{"name":"session","secure":True,"http_only":True,"same_site":"Lax","max_age_seconds":3600,"domain":"app.example.com"}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
