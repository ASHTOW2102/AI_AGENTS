import pytest
from agent import EnvParityAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"name":"production","drift_count":0,"owner":"platform","debug":False,"untracked_overrides":0}]).healthy
def test_risky():assert set(['config_drift','missing_owner','debug_enabled','untracked_overrides']) <= codes(audit([{"name":"staging","drift_count":12,"owner":"","debug":True,"untracked_overrides":3}]))
def test_agent():assert EnvParityAgent().inspect([{"name":"production","drift_count":0,"owner":"platform","debug":False,"untracked_overrides":0}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
