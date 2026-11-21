import unittest
from agent import audit


class KubernetesEphemeralStorageQuotaAuditTests(unittest.TestCase):

    def test_no_limit(self):
        self.assertTrue(audit({"ephemeral_storage_limit_set": False}))

    def test_ok(self):
        self.assertFalse(audit({"ephemeral_storage_limit_set": True, "writes_large_temp_files": True, "ephemeral_storage_limit_mb": 2000, "expected_temp_usage_mb": 500}))
