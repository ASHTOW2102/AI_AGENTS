import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_interpolation(self):self.assertFalse(analyze([{"query":"q","template":"SELECT * FROM t WHERE id = "+chr(36)+"{input}"}])["healthy"])
 def test_bound_parameter(self):self.assertTrue(analyze([{"query":"q","template":"SELECT * FROM t WHERE id = ?","parameterized":True}])["healthy"])
