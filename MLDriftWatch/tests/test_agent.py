import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_drift(self): self.assertEqual(2,len(analyze([{"feature":"age","baseline_mean":10,"current_mean":20,"baseline_std":1,"current_missing_rate":.2}])["findings"]))
 def test_ok(self): self.assertTrue(analyze([{"feature":"age","baseline_mean":10,"current_mean":11,"baseline_std":2}])["healthy"])
