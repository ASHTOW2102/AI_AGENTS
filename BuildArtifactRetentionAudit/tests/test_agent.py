import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"artifact":"release","retention_days":0,"production":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"artifact":"release","retention_days":30,"production":True,"access_policy":"team","cleanup_owner":"ops"}])["healthy"])
