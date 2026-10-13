import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
from agent import analyze
class Tests(unittest.TestCase):
    def test_flags_unsafe_wildcard(self):
        r=analyze([{"origin":"*","allow_credentials":True,"methods":["DELETE"],"headers":["*"]}])
        self.assertFalse(r["healthy"]); self.assertEqual(3, len(r["findings"]))
    def test_safe_origin(self):
        self.assertTrue(analyze([{"origin":"https://app.example","allow_credentials":True,"methods":["GET"],"headers":[]}])["healthy"])
