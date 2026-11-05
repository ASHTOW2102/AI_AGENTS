import unittest
from agent import audit


class ContainerResourceLimitEnforcementAuditTests(unittest.TestCase):

    def test_no_limit_range(self):
        self.assertTrue(audit({"limit_range_defined": False}))

    def test_ok(self):
        self.assertFalse(audit({"limit_range_defined": True, "resource_quota_defined": True, "pods_without_limits_count": 0}))
