import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_bad(self):self.assertEqual(3,len(analyze([{"path":"a-b","p95_ms":500,"packet_loss_percent":5}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"path":"a-b","p95_ms":10,"packet_loss_percent":0,"owner":"o"}])["healthy"])
