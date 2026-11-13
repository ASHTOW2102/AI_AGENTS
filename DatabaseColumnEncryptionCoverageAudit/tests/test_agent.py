import unittest
from agent import audit


class DatabaseColumnEncryptionCoverageAuditTests(unittest.TestCase):

    def test_unencrypted(self):
        self.assertTrue(audit({"sensitive_columns": ["ssn"], "encrypted_columns": []}))

    def test_ok(self):
        self.assertFalse(audit({"sensitive_columns": ["ssn"], "encrypted_columns": ["ssn"], "key_managed_by_kms": True}))
