import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self): self.assertEqual(4,len(analyze([{"dataset":"users","contains_personal_data":True}])["findings"]))
 def test_ok(self): self.assertTrue(analyze([{"dataset":"x","owner":"a","source":"s","updated_at":"2026-01-01"}])["healthy"])
