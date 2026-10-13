import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
from agent import analyze
class Tests(unittest.TestCase):
    def test_replacement(self):
        r=analyze({"resource_changes":[{"address":"aws_db_instance.x","change":{"actions":["delete","create"]}}]})
        self.assertEqual({"replacement","sensitive_change"},{x["code"] for x in r["findings"]})
    def test_noop(self): self.assertTrue(analyze({"resource_changes":[{"address":"x","change":{"actions":["no-op"]}}]})["healthy"])
