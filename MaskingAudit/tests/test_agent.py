import pytest
from agent import MaskingAuditAgent, audit

def codes(report): return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"field":"email","classification":"personal","masked":True,"reversible":False,"sample_present":False,"owner":"privacy"}]).healthy

def test_risky_input_is_detected():
    assert {"unmasked_sensitive","reversible_masking","sample_exposed","missing_owner"} <= codes(audit([{"field":"card_number","classification":"payment","masked":False,"reversible":True,"sample_present":True,"owner":""}]))

def test_agent_delegates():
    assert MaskingAuditAgent().inspect([{"field":"email","classification":"personal","masked":True,"reversible":False,"sample_present":False,"owner":"privacy"}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"): audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"): audit(["bad"])
