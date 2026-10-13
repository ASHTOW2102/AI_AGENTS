import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_flags(self):
  r=analyze([{"timestamp":"2026-01-02T00:00:00Z","actor":"a"},{"timestamp":"2026-01-01T00:00:00Z","type":"decision"}]); self.assertEqual(3,len(r["findings"]))
 def test_ok(self): self.assertTrue(analyze([{"timestamp":"2026-01-01T00:00:00Z","actor":"a"}])["healthy"])
