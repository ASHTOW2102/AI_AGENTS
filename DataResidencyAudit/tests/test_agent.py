import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_violation(self):self.assertEqual(1,len(analyze([{"dataset":"x","region":"US","allowed_regions":["GB"],"owner":"o","personal_data":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"dataset":"x","region":"GB","allowed_regions":["GB"],"owner":"o"}])["healthy"])
