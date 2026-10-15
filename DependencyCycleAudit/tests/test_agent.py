import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_cycle(self): self.assertFalse(analyze({"a":["b"],"b":["a"]})["healthy"])
 def test_dag(self): self.assertTrue(analyze({"a":["b"],"b":[]})["healthy"])
