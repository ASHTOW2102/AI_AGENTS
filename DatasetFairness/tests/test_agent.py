import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_gap(self): self.assertFalse(analyze([{"name":"a","total":100,"positive":90},{"name":"b","total":100,"positive":50}])["healthy"])
 def test_equal(self): self.assertTrue(analyze([{"name":"a","total":10,"positive":5},{"name":"b","total":10,"positive":5}])["healthy"])
