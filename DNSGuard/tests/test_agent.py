import pytest
from agent import DNSGuardAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"domain":"example.com","spf":True,"dmarc":True,"caa":True,"wildcard":False}]).healthy

def test_risky_input_is_detected():
    assert {"missing_spf","missing_dmarc","missing_caa","wildcard_record"} <= codes(audit([{"domain":"legacy.example","spf":False,"dmarc":False,"caa":False,"wildcard":True}]))

def test_agent_delegates():
    assert DNSGuardAgent().inspect([{"domain":"example.com","spf":True,"dmarc":True,"caa":True,"wildcard":False}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
