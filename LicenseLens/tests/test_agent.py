import pytest
from agent import LicenseLensAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"requests","license":"Apache-2.0","attribution_present":True,"approved":True}]).healthy

def test_risky_input_is_detected():
    assert {"unknown_license","unapproved_license","missing_attribution"} <= codes(audit([{"name":"mystery","license":"UNKNOWN","attribution_present":False,"approved":False}]))

def test_agent_delegates():
    assert LicenseLensAgent().inspect([{"name":"requests","license":"Apache-2.0","attribution_present":True,"approved":True}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"):
        audit(["bad"])
