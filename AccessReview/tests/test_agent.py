import pytest
from agent import AccessReviewAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"user":"alex","role":"viewer","inactive_days":5,"owner":"analytics","reviewed_days_ago":20}]).healthy

def test_risky_input_is_detected():
    assert {"dormant_account","privileged_account","missing_owner","never_reviewed"} <= codes(audit([{"user":"old-admin","role":"admin","inactive_days":180,"owner":"","reviewed_days_ago":None}]))

def test_agent_delegates_to_audit():
    assert AccessReviewAgent().inspect([{"user":"alex","role":"viewer","inactive_days":5,"owner":"analytics","reviewed_days_ago":20}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
