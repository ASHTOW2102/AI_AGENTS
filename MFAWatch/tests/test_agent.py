import pytest
from agent import MFAWatchAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"user":"alex","role":"member","mfa":True,"factors":["webauthn"],"inactive_days":2,"recovery":True}]).healthy

def test_risky_input_is_detected():
    assert {"mfa_missing","weak_factor","dormant_admin","missing_recovery"} <= codes(audit([{"user":"root-old","role":"admin","mfa":False,"factors":["sms"],"inactive_days":180,"recovery":False}]))

def test_agent_delegates():
    assert MFAWatchAgent().inspect([{"user":"alex","role":"member","mfa":True,"factors":["webauthn"],"inactive_days":2,"recovery":True}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"):
        audit(["bad"])
