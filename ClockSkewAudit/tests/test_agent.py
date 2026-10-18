import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"node":"n","skew_ms":2000}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"node":"n","skew_ms":5,"time_source":"ntp","monitoring":True}])["healthy"])
