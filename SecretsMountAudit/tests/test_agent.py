import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(4,len(analyze([{"workload":"x","mounted_as_env":True,"shared_across_workloads":True}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"workload":"x","read_only":True,"rotation":True}])["healthy"])
