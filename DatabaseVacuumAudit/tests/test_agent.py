import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_risks(self):self.assertEqual(3,len(analyze([{"table":"events","dead_tuple_percent":40,"seconds_since_vacuum":900000,"transaction_id_age_percent":90}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"table":"events","dead_tuple_percent":1,"seconds_since_vacuum":60}])["healthy"])
