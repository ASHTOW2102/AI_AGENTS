import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_flags(self): self.assertEqual(3,len(analyze([{"answer":"Definitely true","requires_sources":True,"confidence":2}])["findings"]))
 def test_ok(self): self.assertTrue(analyze([{"answer":"Likely","citations":["s"],"requires_sources":True,"confidence":.7}])["healthy"])
