import pytest
from agent import PromptVersionAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"prompt":"support-summary","version":"3.2","owner":"support-ai","evaluated":True,"change_notes":True,"rollback":True}]).healthy
def test_risky():assert set(['missing_version','missing_owner','missing_evaluation','missing_change_notes','missing_rollback'])<=codes(audit([{"prompt":"agent-system","version":"","owner":"","evaluated":False,"change_notes":False,"rollback":False}]))
def test_agent():assert PromptVersionAgent().inspect([{"prompt":"support-summary","version":"3.2","owner":"support-ai","evaluated":True,"change_notes":True,"rollback":True}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
