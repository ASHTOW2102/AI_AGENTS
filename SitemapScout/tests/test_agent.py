import pytest
from agent import SitemapScoutAgent, audit

def codes(report): return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"url":"https://example.com/","last_modified_days":2,"priority":1.0}]).healthy

def test_risky_input_is_detected():
    assert {"insecure_url","stale_page","invalid_priority"} <= codes(audit([{"url":"http://example.com/old","last_modified_days":800,"priority":2.0}]))

def test_agent_delegates():
    assert SitemapScoutAgent().inspect([{"url":"https://example.com/","last_modified_days":2,"priority":1.0}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"): audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"): audit(["bad"])
