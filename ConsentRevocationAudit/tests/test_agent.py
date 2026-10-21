import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_unconfirmed(self):self.assertEqual(1,len(analyze([{"subject_id":"u","revoked_at":"2026-01-01","systems":["crm"],"evidence_reference":"e"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"subject_id":"u","revoked_at":"2026-01-01","systems":["crm"],"confirmed_removed_from":["crm"],"evidence_reference":"e"}])["healthy"])
