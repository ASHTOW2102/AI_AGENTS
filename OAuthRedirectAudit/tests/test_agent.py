import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"client":"x","redirect_uris":["http://example.com/*"]}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"client":"x","redirect_uris":["https://example.com/cb"],"pkce_required":True}])["healthy"])
