import pytest
from agent import CertWatchAgent, audit

def codes(report):
    return {item.code for item in report.findings}

def test_healthy_input_passes():
    assert audit([{"hostname":"api.example.com","days_remaining":90,"names":["api.example.com"],"key_bits":2048,"trusted":True}]).healthy

def test_risky_input_is_detected():
    assert {"expires_soon", "hostname_mismatch", "weak_key", "untrusted_chain"} <= codes(audit([{"hostname":"shop.example.com","days_remaining":5,"names":["old.example.com"],"key_bits":1024,"trusted":False}]))

def test_agent_delegates_to_audit():
    assert CertWatchAgent().inspect([{"hostname":"api.example.com","days_remaining":90,"names":["api.example.com"],"key_bits":2048,"trusted":True}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
