import unittest
from agent import audit


class CloudEgressDNSAuditTests(unittest.TestCase):
    def test_open_egress(self):
        self.assertIn("unrestricted", audit({"unrestricted_egress_rules": 1})[0]["issue"])

    def test_restricted_policy(self):
        policy = {"unrestricted_egress_rules": 0, "dns_egress_required": True,
                  "approved_dns_resolver_only": True, "egress_restrictions_enabled": True,
                  "egress_flow_logging": True, "sensitive_workload": True,
                  "public_internet_egress": False}
        self.assertEqual([], audit(policy))


if __name__ == "__main__":
    unittest.main()
