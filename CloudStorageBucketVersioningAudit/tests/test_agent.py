import unittest
from agent import audit


class CloudStorageBucketVersioningAuditTests(unittest.TestCase):

    def test_no_versioning(self):
        self.assertTrue(audit({"versioning_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"versioning_enabled": True, "lifecycle_policy_configured": True}))
