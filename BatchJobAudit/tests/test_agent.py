import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(4,len(analyze([{"job":"x","duration_minutes":100}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"job":"x","duration_minutes":10,"idempotent":1,"owner":"o"}])["healthy"])
