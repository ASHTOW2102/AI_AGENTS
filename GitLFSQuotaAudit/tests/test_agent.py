import unittest
from agent import audit


class GitLFSQuotaAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"lfs_usage_bytes": 950, "lfs_quota_bytes": 1000}))

    def test_ok(self):
        self.assertFalse(audit({"lfs_usage_bytes": 400, "lfs_quota_bytes": 1000}))
