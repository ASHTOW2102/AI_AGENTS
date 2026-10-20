import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"experiment":"checkout"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"experiment":"checkout","primary_metric":"conversion","guardrail_metrics":["errors"],"exposure_logging":1,"end_date":"2026-12-01","mutually_exclusive":True}])["healthy"])
