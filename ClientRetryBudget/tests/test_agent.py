import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_risks(self):self.assertEqual(4,len(analyze([{"client":"sdk","max_retries":8,"max_delay_ms":1000}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"client":"sdk","max_retries":2,"max_delay_ms":500,"backoff":True,"jitter":True,"overall_deadline_ms":2000}])["healthy"])
