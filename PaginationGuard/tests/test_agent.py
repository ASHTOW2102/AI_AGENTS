import pytest
from agent import PaginationGuardAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"endpoint":"/orders","default_limit":50,"max_limit":200,"stable_sort":True,"continuation_token":True}]).healthy
def test_risky():assert {"no_default_limit","excessive_max_limit","unstable_sort","missing_token"} <= codes(audit([{"endpoint":"/events","default_limit":None,"max_limit":10000,"stable_sort":False,"continuation_token":False}]))
def test_agent():assert PaginationGuardAgent().inspect([{"endpoint":"/orders","default_limit":50,"max_limit":200,"stable_sort":True,"continuation_token":True}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
