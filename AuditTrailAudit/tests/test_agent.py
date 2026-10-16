import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_missing(self): self.assertEqual(4,len(analyze([{"event_id":"1"}])["findings"]))
 def test_ok(self): self.assertTrue(analyze([{"event_id":"1","timestamp":"t","actor":"a","action":"x","target":"y"}])["healthy"])
