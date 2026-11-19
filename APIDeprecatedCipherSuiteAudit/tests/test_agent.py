import unittest
from agent import audit


class APIDeprecatedCipherSuiteAuditTests(unittest.TestCase):

    def test_weak_cipher(self):
        self.assertTrue(audit({"offered_ciphers": ["TLS_RSA_WITH_RC4_128_SHA"]}))

    def test_ok(self):
        self.assertFalse(audit({"offered_ciphers": ["TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"], "forward_secrecy_enforced": True}))
