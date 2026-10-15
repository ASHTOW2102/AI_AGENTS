import sys,unittest
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self): self.assertEqual(4,len(analyze([{"service":"db"}],date(2026,1,1))["findings"]))
 def test_ok(self): self.assertTrue(analyze([{"service":"db","rto_minutes":30,"rpo_minutes":5,"last_tested":"2025-12-01","owner":"ops"}],date(2026,1,1))["healthy"])
