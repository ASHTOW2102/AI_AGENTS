import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_breaches(self):self.assertEqual(3,len(analyze([{"model":"m","p99_latency_ms":500,"latency_target_ms":200,"availability_percent":90,"availability_goal_percent":99}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"model":"m","p99_latency_ms":10,"latency_target_ms":20,"availability_percent":99.9,"availability_goal_percent":99,"capacity_alert":True}])["healthy"])
