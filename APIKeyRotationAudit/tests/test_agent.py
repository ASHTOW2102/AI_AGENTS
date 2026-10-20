import sys,unittest
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_missing(self):self.assertEqual(3,len(analyze([{"key_id":"k"}],date(2026,1,1))["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"key_id":"k","owner":"o","scope":"read","last_rotated":"2025-12-15"}],date(2026,1,1))["healthy"])
