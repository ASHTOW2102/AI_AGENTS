import unittest
from agent import audit


class TenantQuotaIsolationAuditTests(unittest.TestCase):
    def test_unbound_quota_check(self):
        self.assertIn("authenticated tenant", audit({"quota_usage_check": True,
                                                      "tenant_id_bound_to_identity": False})[0]["issue"])

    def test_isolated_quota(self):
        service = {"multi_tenant": True, "quota_enforced_per_tenant": True,
                   "tenant_override_count": 0, "quota_usage_check": True,
                   "tenant_id_bound_to_identity": True, "quota_exhaustion_alert": True}
        self.assertEqual([], audit(service))


if __name__ == "__main__":
    unittest.main()
