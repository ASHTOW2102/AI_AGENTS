import unittest
from agent import audit


class ContainerImageSignatureExpiryAuditTests(unittest.TestCase):

    def test_missing_signature(self):
        self.assertTrue(audit({"signature_present": False}))

    def test_ok(self):
        self.assertFalse(audit({"signature_present": True, "signature_expired": False, "verification_enforced": True}))
