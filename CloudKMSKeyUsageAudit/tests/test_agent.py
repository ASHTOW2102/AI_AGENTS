import unittest
from agent import audit


class CloudKMSKeyUsageAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"allows_decrypt_from_any_principal": True}))

    def test_ok(self):
        self.assertFalse(audit({"allows_decrypt_from_any_principal": False}))
