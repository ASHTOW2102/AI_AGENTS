import unittest
from agent import audit


class SecretScopeConsistencyAuditTests(unittest.TestCase):
    def test_wildcard_secret_access(self):
        self.assertEqual("critical", audit({"wildcard_access": True})[-1]["severity"])

    def test_narrow_scope(self):
        secret = {"authorized_workloads": ["api"], "required_workloads": ["api"],
                  "shared_across_environments": False, "workload_identity_binding": True,
                  "wildcard_access": False}
        self.assertEqual([], audit(secret))


if __name__ == "__main__":
    unittest.main()
