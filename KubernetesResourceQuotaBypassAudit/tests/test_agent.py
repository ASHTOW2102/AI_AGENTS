import unittest
from agent import audit


class KubernetesResourceQuotaBypassAuditTests(unittest.TestCase):

    def test_bypassable(self):
        self.assertTrue(audit({"has_resource_quota": True, "limit_range_defaults_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"has_resource_quota": True, "limit_range_defaults_configured": True, "pods_without_requests_count": 0}))
