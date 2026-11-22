import unittest
from agent import audit


class TLSCipherSuiteAuditTests(unittest.TestCase):

    def test_weak_cipher(self):
        self.assertTrue(audit({"enabled_cipher_suites": ["AES256-GCM", "RC4"], "min_protocol_version": "TLS1.2"}))

    def test_ok(self):
        self.assertFalse(audit({"enabled_cipher_suites": ["AES256-GCM", "CHACHA20"], "min_protocol_version": "TLS1.2"}))
