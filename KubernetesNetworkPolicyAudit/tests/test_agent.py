import unittest
from agent import audit


class KubernetesNetworkPolicyAuditTests(unittest.TestCase):
    def test_missing_default_deny(self):
        findings = audit({})
        self.assertEqual(2, len(findings))

    def test_isolated_namespace(self):
        self.assertEqual([], audit({"default_deny_ingress": True, "default_deny_egress": True,
                                    "public_workloads": 0, "unrestricted_egress_rules": 0}))


if __name__ == "__main__":
    unittest.main()
