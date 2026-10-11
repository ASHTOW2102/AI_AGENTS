import pytest
from agent import PasswordGuardAgent, audit

def codes(report): return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"application":"portal","min_length":14,"breach_check":True,"secure_reset":True,"lockout_attempts":5}]).healthy

def test_risky_input_is_detected():
    assert {"short_password","missing_breach_check","unsafe_reset","no_lockout"} <= codes(audit([{"application":"legacy","min_length":6,"breach_check":False,"secure_reset":False,"lockout_attempts":None}]))

def test_agent_delegates():
    assert PasswordGuardAgent().inspect([{"application":"portal","min_length":14,"breach_check":True,"secure_reset":True,"lockout_attempts":5}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"): audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"): audit(["bad"])
