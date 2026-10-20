import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"hostname":"api"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"hostname":"api","chain_complete":1,"hostname_match":1,"trusted_root":1,"revocation_checked":1}])["healthy"])
