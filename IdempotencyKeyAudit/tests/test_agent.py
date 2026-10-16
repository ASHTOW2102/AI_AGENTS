import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_missing(self):self.assertFalse(analyze([{"route":"/pay","method":"POST"}])["healthy"])
 def test_ok(self):self.assertTrue(analyze([{"route":"/pay","method":"POST","idempotency_key":True,"ttl_seconds":60,"request_fingerprint":True}])["healthy"])
