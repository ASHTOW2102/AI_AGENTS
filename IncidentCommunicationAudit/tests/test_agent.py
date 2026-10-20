import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(2,len(analyze([{"incident_id":"i","updates":[]}])["findings"]))
 def test_ok(self):
  u={"timestamp":"t","audience":"users","channel":"status","summary":"Investigating","next_update_at":"later"}
  self.assertTrue(analyze([{"incident_id":"i","updates":[u],"communications_owner":"ops"}])["healthy"])
