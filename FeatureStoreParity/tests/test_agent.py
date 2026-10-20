import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gap(self):self.assertEqual(3,len(analyze([{"feature":"f","offline_mean":0,"online_mean":2,"tolerance":.1,"offline_version":"1","online_version":"2"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"feature":"f","offline_mean":2,"online_mean":2,"tolerance":0,"offline_version":"1","online_version":"1","owner":"x"}])["healthy"])
