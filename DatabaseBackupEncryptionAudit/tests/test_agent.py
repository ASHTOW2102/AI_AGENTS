import unittest
from agent import audit


class DatabaseBackupEncryptionAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"encrypted_at_rest": False}))

    def test_ok(self):
        self.assertFalse(audit({"encrypted_at_rest": True}))
