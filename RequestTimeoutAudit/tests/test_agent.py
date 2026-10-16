import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"dependency":"x","retries":2}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"dependency":"x","connect_ms":100,"read_ms":1000}])["healthy"])
