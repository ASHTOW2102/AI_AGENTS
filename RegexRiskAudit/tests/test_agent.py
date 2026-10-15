import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_nested(self): self.assertFalse(analyze([{"name":"x","pattern":"(a+)+$"}])["healthy"])
 def test_ok(self): self.assertTrue(analyze([{"name":"x","pattern":"^[a-z]+$"}])["healthy"])
