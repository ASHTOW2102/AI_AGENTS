import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"name":"x","url":"http://example.com"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"name":"x","url":"https://example.com","owner":"o","data_classification":"public","timeout_ms":100}])["healthy"])
