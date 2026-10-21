import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"route":"/x","accepts_body":True,"json_contract":True,"produces":["*/*"]}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"route":"/x","produces":["application/json"],"consumes":["application/json"],"accepts_body":True}])["healthy"])
