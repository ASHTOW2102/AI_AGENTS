import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"deployment":"v2","error_rate":.5,"latency_ms":2000}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"deployment":"v2","healthy_instances":2,"rollback_automated":True}])["healthy"])
