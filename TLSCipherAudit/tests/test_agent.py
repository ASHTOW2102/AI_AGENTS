import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]));from agent import analyze
class T(unittest.TestCase):
 def test_weak(self):self.assertEqual(3,len(analyze([{"endpoint":"api","ciphers":["3DES"],"min_tls":"TLS1.0"}])["findings"]))
 def test_ok(self):self.assertTrue(analyze([{"endpoint":"api","ciphers":["TLS_AES_128_GCM_SHA256"],"min_tls":"TLS1.2","forward_secrecy":True}])["healthy"])
