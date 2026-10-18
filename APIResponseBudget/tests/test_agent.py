import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"route":"/x","bytes":2000000,"collection":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"route":"/x","bytes":10}])["healthy"])
