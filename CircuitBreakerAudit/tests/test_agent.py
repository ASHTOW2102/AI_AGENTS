import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"dependency":"pay"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"dependency":"pay","failure_threshold":5,"reset_seconds":30,"fallback":"queue","metrics":True}])["healthy"])
