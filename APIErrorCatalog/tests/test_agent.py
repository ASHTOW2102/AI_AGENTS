import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_risks(self): self.assertEqual(2,len(analyze([{"code":"E","status":500,"message":"x","exposes_stack":True}])["findings"]))
 def test_ok(self): self.assertTrue(analyze([{"code":"BAD_INPUT","status":400,"message":"Check input"}])["healthy"])
