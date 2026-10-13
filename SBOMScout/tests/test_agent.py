import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
from agent import analyze
class Tests(unittest.TestCase):
    def test_gaps(self): self.assertEqual(4,len(analyze({"components":[{"name":"x","scope":"required"}]})["findings"]))
    def test_complete(self):
        c={"name":"x","version":"1","purl":"pkg:pypi/x@1","licenses":["MIT"],"scope":"required","hashes":["abc"]}
        self.assertTrue(analyze({"components":[c]})["healthy"])
