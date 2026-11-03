import unittest
from agent import audit


class DataExportEncryptionAuditTests(unittest.TestCase):

    def test_unencrypted_sensitive(self):
        self.assertTrue(audit({"contains_sensitive_data": True, "file_encrypted": False}))

    def test_ok(self):
        self.assertFalse(audit({"contains_sensitive_data": True, "file_encrypted": True, "key_shared_via_secure_channel": True, "transfer_protocol": "sftp"}))
