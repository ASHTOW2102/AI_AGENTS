import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_credential(self):self.assertFalse(analyze([{"application":"app","entries":[{"key":"access_token","storage":"localStorage"}]}])["healthy"])
 def test_ok(self):self.assertTrue(analyze([{"application":"app","entries":[{"key":"theme","storage":"localStorage"}]}])["healthy"])
