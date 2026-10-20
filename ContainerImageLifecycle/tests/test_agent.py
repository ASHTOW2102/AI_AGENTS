import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(5,len(analyze([{"image":"app","tag":"latest","runs_as_root":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"image":"app","digest":"sha256:"+"a"*64,"source_repository":"r","rebuild_policy_days":30}])["healthy"])
