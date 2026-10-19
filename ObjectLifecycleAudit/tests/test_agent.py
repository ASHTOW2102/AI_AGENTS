import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(4,len(analyze([{"bucket":"b","versioning":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"bucket":"b","expiration_days":30,"abort_incomplete_upload_days":1,"owner":"o"}])["healthy"])
