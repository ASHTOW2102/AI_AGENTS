import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(3,len(analyze([{"deployment":"v2","canary_error_rate":.2,"baseline_error_rate":.01,"canary_latency_ms":200,"baseline_latency_ms":100}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"deployment":"v2","canary_error_rate":0,"baseline_error_rate":0,"sample_size":100}])["healthy"])
