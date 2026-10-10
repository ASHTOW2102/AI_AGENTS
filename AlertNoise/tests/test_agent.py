import pytest
from agent import AlertNoiseAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"API down","owner":"platform","fires_per_day":0.2,"runbook":True,"message":"API unavailable in region"}]).healthy

def test_risky_input_is_detected():
    assert {"missing_owner","noisy_alert","missing_runbook","vague_message"} <= codes(audit([{"name":"Error","owner":"","fires_per_day":200,"runbook":False,"message":"Something happened"}]))

def test_agent_delegates():
    assert AlertNoiseAgent().inspect([{"name":"API down","owner":"platform","fires_per_day":0.2,"runbook":True,"message":"API unavailable in region"}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"):
        audit(["bad"])
