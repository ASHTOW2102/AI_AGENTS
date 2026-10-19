import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(4,len(analyze([{"resource":"orders","shared_cache":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"resource":"orders","tenant_key":"id","authorization_filter":1,"isolation_tests":1}])["healthy"])
