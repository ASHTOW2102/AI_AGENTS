import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(3,len(analyze([{"service":"x","desired":1,"ready":0,"critical":True,"variable_load":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"service":"x","desired":2,"ready":2}])["healthy"])
