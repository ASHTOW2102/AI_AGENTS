import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"index":"x","documents":1,"source_documents":100}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"index":"x","documents":100,"source_documents":100,"last_indexed_at":"t","owner":"o"}])["healthy"])
