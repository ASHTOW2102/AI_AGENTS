import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_near(self):self.assertEqual(2,len(analyze([{"namespace":"prod","used":{"pods":9},"limit":{"pods":10}}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"namespace":"dev","used":{"pods":2},"limit":{"pods":10},"owner":"team"}])["healthy"])
