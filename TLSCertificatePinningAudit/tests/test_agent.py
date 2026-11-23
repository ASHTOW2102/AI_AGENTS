import unittest
from agent import audit


class TLSCertificatePinningAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"handles_sensitive_data": True, "certificate_pinning_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"handles_sensitive_data": True, "certificate_pinning_enabled": True}))
