import unittest
from agent import audit


class KubernetesSecretEncryptionAtRestAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"etcd_encryption_at_rest_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"etcd_encryption_at_rest_enabled": True}))
