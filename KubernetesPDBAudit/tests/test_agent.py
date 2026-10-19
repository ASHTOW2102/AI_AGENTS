import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_missing(self):self.assertFalse(analyze([{"workload":"x","replicas":3}])["healthy"])
 def test_ok(self):self.assertTrue(analyze([{"workload":"x","replicas":3,"min_available":2}])["healthy"])
