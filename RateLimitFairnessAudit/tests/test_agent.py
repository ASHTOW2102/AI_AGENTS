import unittest
from agent import audit


class RateLimitFairnessAuditTests(unittest.TestCase):
    def test_global_only_multi_tenant_limit(self):
        self.assertIn("per-tenant", audit({"multi_tenant": True})[0]["issue"])

    def test_fair_policy(self):
        policy = {"multi_tenant": True, "per_tenant_partitioning": True, "tenant_limit": 50,
                  "approved_tenant_limit": 100, "limit_rejection_metric": True}
        self.assertEqual([], audit(policy))


if __name__ == "__main__":
    unittest.main()
