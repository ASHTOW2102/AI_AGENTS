import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_failures(self): self.assertEqual(3,len(analyze([{"dataset":"x","rows":10,"null_rows":2,"duplicate_rows":1,"min_rows":20}])["findings"]))
 def test_ok(self): self.assertTrue(analyze([{"dataset":"x","rows":100,"max_null_rate":.1,"max_duplicate_rate":.1}])["healthy"])
