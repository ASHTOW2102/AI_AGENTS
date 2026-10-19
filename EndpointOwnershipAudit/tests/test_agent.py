import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(4,len(analyze([{"endpoint":"/x"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"endpoint":"/x","team":"t","repository":"r","on_call":"o","runbook":"b"}])["healthy"])
