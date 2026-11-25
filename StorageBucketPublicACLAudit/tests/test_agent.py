import unittest
from agent import audit


class StorageBucketPublicACLAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"public_read_acl": True, "contains_sensitive_data": True}))

    def test_ok(self):
        self.assertFalse(audit({"public_read_acl": False}))
