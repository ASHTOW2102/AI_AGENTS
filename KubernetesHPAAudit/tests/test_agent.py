import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_gaps(self):self.assertEqual(3,len(analyze([{"workload":"api","min_replicas":1,"max_replicas":10,"cpu_request_defined":False}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"workload":"api","min_replicas":1,"max_replicas":4,"metrics":["cpu"],"cpu_request_defined":True,"scale_down_stabilization_seconds":60}])["healthy"])
