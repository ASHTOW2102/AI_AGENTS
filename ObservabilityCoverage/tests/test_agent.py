import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(5,len(analyze([{"service":"x"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"service":"x","logs":1,"metrics":1,"traces":1,"dashboard":1,"alerts":1,"runbook":1}])["healthy"])
