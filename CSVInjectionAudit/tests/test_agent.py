import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_formula(self):self.assertFalse(analyze([["name"],["=1+1"]])["healthy"])
 def test_text(self):self.assertTrue(analyze([["name"],["Alice"]])["healthy"])
