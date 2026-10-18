import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class Tests(unittest.TestCase):
 def test_gaps(self):self.assertEqual(4,len(analyze([{"database":"db","min_connections":0,"max_connections":20,"database_limit":10}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"database":"db","min_connections":1,"max_connections":10,"database_limit":20,"acquire_timeout_ms":100,"idle_timeout_ms":1000,"metrics":True}])["healthy"])
