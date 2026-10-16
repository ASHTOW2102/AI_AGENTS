import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"route":"/x","personalized":True,"varies_by_language":True,"varies_by_query":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"route":"/x","key_parts":["user_id","language","query"],"personalized":True,"varies_by_language":True,"varies_by_query":True,"ttl_seconds":60}])["healthy"])
