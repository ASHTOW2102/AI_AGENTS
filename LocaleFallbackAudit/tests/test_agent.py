import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"message_key":"hello","default_locale":"en","locales":{"fr":""}}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"message_key":"hello","default_locale":"en","locales":{"en":"Hi"},"fallback_chain":["en"]}])["healthy"])
