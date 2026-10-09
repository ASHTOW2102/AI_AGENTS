import pytest
from agent import ConsentLedgerAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"subject_id":"u1","purpose":"email_marketing","evidence":True,"age_days":20,"valid_days":365,"withdrawal_available":True}]).healthy

def test_risky_input_is_detected():
    assert {"missing_evidence","vague_purpose","expired_consent","no_withdrawal"} <= codes(audit([{"subject_id":"u2","purpose":"all","evidence":False,"age_days":500,"valid_days":365,"withdrawal_available":False}]))

def test_agent_delegates():
    assert ConsentLedgerAgent().inspect([{"subject_id":"u1","purpose":"email_marketing","evidence":True,"age_days":20,"valid_days":365,"withdrawal_available":True}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
