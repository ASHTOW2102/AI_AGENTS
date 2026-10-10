import pytest
from agent import ImageBudgetAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"path":"hero.webp","bytes":120000,"width":1200,"height":600,"alt":"Team working","format":"webp"}]).healthy

def test_risky_input_is_detected():
    assert {"oversized_image","missing_dimensions","missing_alt","inefficient_format"} <= codes(audit([{"path":"banner.bmp","bytes":3000000,"width":None,"height":None,"alt":"","format":"bmp"}]))

def test_agent_delegates():
    assert ImageBudgetAgent().inspect([{"path":"hero.webp","bytes":120000,"width":1200,"height":600,"alt":"Team working","format":"webp"}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"):
        audit(["bad"])
