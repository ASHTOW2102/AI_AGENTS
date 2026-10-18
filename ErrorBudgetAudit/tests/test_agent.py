import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_exhausted(self):self.assertEqual(2,len(analyze([{"service":"x","budget_minutes":10,"spent_minutes":20}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"service":"x","budget_minutes":10,"spent_minutes":0}])["healthy"])
