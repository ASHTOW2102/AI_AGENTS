import pytest
from agent import PatchWindowAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"component":"gateway","severity":"medium","age_days":10,"sla_days":30,"owner":"platform","window":True,"tested":True}]).healthy
def test_risky():assert set(['patch_overdue','missing_owner','missing_window','untested_patch'])<=codes(audit([{"component":"kernel","severity":"critical","age_days":90,"sla_days":7,"owner":"","window":False,"tested":False}]))
def test_agent():assert PatchWindowAgent().inspect([{"component":"gateway","severity":"medium","age_days":10,"sla_days":30,"owner":"platform","window":True,"tested":True}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
