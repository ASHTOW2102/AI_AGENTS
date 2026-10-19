import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(4,len(analyze([{"name":"lb","cross_zone":False,"zones":2}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"name":"lb","health_check":1,"connection_draining":1,"cross_zone":True,"zones":2,"tls_policy":"modern"}])["healthy"])
