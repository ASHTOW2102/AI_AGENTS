import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(5,len(analyze([{"route":"/ws"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"route":"/ws","origin_allowlist":["x"],"authentication":True,"max_message_bytes":10,"idle_timeout_seconds":10,"rate_limit":5}])["healthy"])
