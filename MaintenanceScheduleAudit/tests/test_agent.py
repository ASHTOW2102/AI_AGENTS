import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"service":"x","start":"2026-01-01T02:00:00Z","end":"2026-01-01T01:00:00Z","customer_impact":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"service":"x","start":"2026-01-01T01:00:00Z","end":"2026-01-01T02:00:00Z","owner":"o","rollback_plan":"r"}])["healthy"])
