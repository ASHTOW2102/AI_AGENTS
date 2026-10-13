import pytest
from agent import ArtifactIntegrityAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"artifact":"api-2.1.tar","signed":True,"checksum":True,"provenance":True,"immutable":True}]).healthy
def test_risky():assert set(['unsigned_artifact','missing_checksum','missing_provenance','mutable_artifact'])<=codes(audit([{"artifact":"api-latest.tar","signed":False,"checksum":False,"provenance":False,"immutable":False}]))
def test_agent():assert ArtifactIntegrityAgent().inspect([{"artifact":"api-2.1.tar","signed":True,"checksum":True,"provenance":True,"immutable":True}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
