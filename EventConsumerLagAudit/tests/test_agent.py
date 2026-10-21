import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_risks(self):self.assertEqual(4,len(analyze([{"consumer_group":"billing","lag":9000,"oldest_unprocessed_seconds":900,"partitions":8,"active_consumers":2}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"consumer_group":"billing","lag":0,"oldest_unprocessed_seconds":1,"lag_alert":True}])["healthy"])
