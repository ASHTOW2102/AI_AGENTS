import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(3,len(analyze([{"runtime":"jvm","p99_pause_ms":300,"heap_usage_percent":95}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"runtime":"jvm","p99_pause_ms":10,"heap_usage_percent":50,"metrics_enabled":True}])["healthy"])
