import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(3,len(analyze([{"dependency":"pay","availability_target":99.9,"availability_actual":90}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"dependency":"pay","availability_target":99,"availability_actual":100,"support_contact":"x","escalation_minutes":5}])["healthy"])
