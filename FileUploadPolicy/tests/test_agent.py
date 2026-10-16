import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"route":"/upload"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"route":"/u","max_bytes":10,"allowed_types":["png"],"content_sniffing":True,"malware_scan":True}])["healthy"])
