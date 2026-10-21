import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"namespace":"cart","key":"user:email","ephemeral":True,"contains_personal_data":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"namespace":"cart","key":"cart:123","ephemeral":True,"ttl_seconds":60}])["healthy"])
