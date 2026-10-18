import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(5,len(analyze([{"export":"x"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"export":"x","requester_verified":True,"scope_reviewed":True,"encrypted":True,"expires_at":"t","audit_event":"e"}])["healthy"])
