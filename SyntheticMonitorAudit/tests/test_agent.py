import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self): self.assertEqual(4,len(analyze([{"name":"checkout","interval_minutes":30,"critical":True}])["findings"]))
 def test_ok(self): self.assertTrue(analyze([{"name":"x","interval_minutes":5,"alert_route":"ops","locations":["uk","us"],"assertions":["200"]}])["healthy"])
