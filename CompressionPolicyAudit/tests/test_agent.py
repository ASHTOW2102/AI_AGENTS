import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_secret_risk(self):self.assertFalse(analyze([{"route":"/x","algorithms":["br"],"secrets_in_response":True,"compression_over_tls":True}])["healthy"])
 def test_ok(self):self.assertTrue(analyze([{"route":"/x","algorithms":["br"],"content_types":["text/html"]}])["healthy"])
