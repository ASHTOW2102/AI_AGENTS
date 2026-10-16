import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_risk(self):self.assertEqual(2,len(analyze([{"stream":"auth","sample_rate":.5,"security_events":True,"errors":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"stream":"auth","sample_rate":1,"security_events":True}])["healthy"])
