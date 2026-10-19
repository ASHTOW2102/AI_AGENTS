import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(3,len(analyze([{"database":"db","max_wait_seconds":10,"blocked_sessions":2}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"database":"db","max_wait_seconds":0,"blocked_sessions":0}])["healthy"])
