import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"flow":"login"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"flow":"login","rate_limit":1,"progressive_delay":1,"credential_stuffing_detection":1,"account_recovery_rate_limit":1}])["healthy"])
