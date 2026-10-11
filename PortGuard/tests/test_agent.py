import pytest
from agent import PortGuardAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"host":"api","port":443,"protocol":"https","public":True,"owner":"platform","debug":False}]).healthy
def test_risky():assert {"public_admin_port","unencrypted_protocol","missing_owner","debug_service"} <= codes(audit([{"host":"db","port":5432,"protocol":"postgres","public":True,"owner":"","debug":True}]))
def test_agent():assert PortGuardAgent().inspect([{"host":"api","port":443,"protocol":"https","public":True,"owner":"platform","debug":False}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
