import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"app":"mobile","sensitive_action":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"app":"mobile","host_allowlist":["example.com"],"route_authorization":1,"parameter_validation":1}])["healthy"])
