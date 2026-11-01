import unittest
from agent import audit


class TLSMinVersionAuditTests(unittest.TestCase):

    def test_old_tls(self):
        self.assertTrue(audit({"min_tls_version": "1.0"}))

    def test_ok(self):
        self.assertFalse(audit({"min_tls_version": "1.3", "allows_sslv3": False, "weak_cipher_enabled": False}))
