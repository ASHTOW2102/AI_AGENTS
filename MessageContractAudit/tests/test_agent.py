import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"event":"created","breaking_change":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"event":"created","version":"1","schema":"s","owner":"o"}])["healthy"])
