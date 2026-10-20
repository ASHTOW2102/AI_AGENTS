import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(4,len(analyze([{"service":"api","weights":[10,80,60],"max_step_percent":25}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"service":"api","weights":[5,10,20],"health_gate":True}])["healthy"])
