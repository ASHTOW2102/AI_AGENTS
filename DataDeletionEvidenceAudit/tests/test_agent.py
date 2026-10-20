import sys,unittest
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"request_id":"r","due_date":"2025-01-01"}],date(2026,1,1))["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"request_id":"r","verified_request":1,"completed_at":"t","systems_checked":["a"],"evidence_reference":"e"}],date(2026,1,1))["healthy"])
