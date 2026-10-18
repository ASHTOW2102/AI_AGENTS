import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"workload":"x","request_mb":100,"limit_mb":1000,"peak_mb":950}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"workload":"x","request_mb":100,"limit_mb":200,"peak_mb":100,"oom_alert":True}])["healthy"])
