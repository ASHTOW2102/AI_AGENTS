import pytest
from agent import DomainExpiryAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"domain":"example.com","days_remaining":300,"auto_renew":True,"owner":"platform","registrar_lock":True}]).healthy

def test_risky_input_is_detected():
    assert {"expires_soon","auto_renew_off","missing_owner","registrar_unlocked"} <= codes(audit([{"domain":"old.example","days_remaining":5,"auto_renew":False,"owner":"","registrar_lock":False}]))

def test_agent_delegates():
    assert DomainExpiryAgent().inspect([{"domain":"example.com","days_remaining":300,"auto_renew":True,"owner":"platform","registrar_lock":True}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"):
        audit(["bad"])
