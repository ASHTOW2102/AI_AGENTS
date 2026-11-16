import unittest
from agent import audit


class APIWebhookSignatureAuditTests(unittest.TestCase):

    def test_unsigned(self):
        self.assertTrue(audit({"payload_signed": False}))

    def test_ok(self):
        self.assertFalse(audit({"payload_signed": True, "signature_algorithm": "sha256"}))
