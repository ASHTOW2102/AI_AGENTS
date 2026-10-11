import pytest
from agent import ServiceCatalogAgent, audit

def codes(report): return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"checkout","owner":"payments","repository":"org/checkout","tier":1,"docs_age_days":20}]).healthy

def test_risky_input_is_detected():
    assert {"missing_owner","missing_repository","invalid_tier","stale_docs"} <= codes(audit([{"name":"mystery","owner":"","repository":"","tier":9,"docs_age_days":500}]))

def test_agent_delegates():
    assert ServiceCatalogAgent().inspect([{"name":"checkout","owner":"payments","repository":"org/checkout","tier":1,"docs_age_days":20}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"): audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"): audit(["bad"])
