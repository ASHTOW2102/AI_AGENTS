import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_limits(self):self.assertEqual(3,len(analyze([{"operation":"q","depth":20,"cost":2000,"anonymous":True,"introspection":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"operation":"q","depth":2,"cost":10}])["healthy"])
