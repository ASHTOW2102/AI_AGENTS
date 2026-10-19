import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(3,len(analyze([{"service":"x","trace_id":"bad"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"service":"x","trace_id":"a"*32,"parent_propagated":1,"baggage_filtered":1}])["healthy"])
