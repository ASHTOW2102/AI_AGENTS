import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"database":"db","tls_required":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"database":"db","tls_required":True,"certificate_verification":True,"least_privilege_role":"app","network_allowlist":["app"]}])["healthy"])
