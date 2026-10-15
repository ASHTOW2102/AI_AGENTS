import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1])); from agent import analyze
class Tests(unittest.TestCase):
 def test_budget(self):
  x={"name":"x","input_tokens":1000,"output_tokens":3000,"input_cost_per_million":1,"output_cost_per_million":2,"runs_per_day":100,"daily_budget":.1}
  self.assertEqual(2,len(analyze([x])["findings"]))
 def test_ok(self):
  x={"name":"x","input_tokens":100,"output_tokens":100,"input_cost_per_million":1,"output_cost_per_million":1,"runs_per_day":1,"daily_budget":1}
  self.assertTrue(analyze([x])["healthy"])
