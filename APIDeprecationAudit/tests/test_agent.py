import sys,unittest
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self): self.assertEqual(2,len(analyze([{"endpoint":"/v1","deprecated":True}],date(2026,1,1))["findings"]))
 def test_ok(self): self.assertTrue(analyze([{"endpoint":"/v2"}],date(2026,1,1))["healthy"])
