import sys,unittest
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(3,len(analyze([{"service":"x"}],date(2026,1,1))["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"service":"x","procedure":"p","last_tested":"2025-12-01","evidence_link":"e"}],date(2026,1,1))["healthy"])
