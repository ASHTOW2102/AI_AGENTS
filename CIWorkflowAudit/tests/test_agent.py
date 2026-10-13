import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_flags(self): self.assertEqual(3,len(analyze([{"name":"x","permissions":"write-all","pull_request_target":True,"runs_untrusted_code":True,"actions":["a@main"]}])["findings"]))
 def test_ok(self): self.assertTrue(analyze([{"name":"x","permissions":"read","actions":["a@"+"a"*40]}])["healthy"])
