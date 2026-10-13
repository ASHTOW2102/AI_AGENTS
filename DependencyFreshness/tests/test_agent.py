import sys,unittest
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_stale(self): self.assertEqual(2,len(analyze([{"name":"x","released_at":"2020-01-01","version":"1","latest_version":"2"}],date(2026,1,1))["findings"]))
 def test_current(self): self.assertTrue(analyze([{"name":"x","released_at":"2026-01-01","version":"1"}],date(2026,1,2))["healthy"])
