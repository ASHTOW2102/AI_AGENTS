import pytest
from agent import PinDoctorAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"package":"httpx","pinned":True,"age_days":30,"trusted_source":True,"hash_locked":True}]).healthy
def test_risky():assert set(['floating_version','stale_dependency','untrusted_source','missing_hash']) <= codes(audit([{"package":"mystery","pinned":False,"age_days":900,"trusted_source":False,"hash_locked":False}]))
def test_agent():assert PinDoctorAgent().inspect([{"package":"httpx","pinned":True,"age_days":30,"trusted_source":True,"hash_locked":True}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
