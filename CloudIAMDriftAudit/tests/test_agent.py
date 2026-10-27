import unittest
from agent import audit


class CloudIAMDriftAuditTests(unittest.TestCase):
    def test_excess_privilege(self):
        self.assertIn("delete", audit({"granted_actions": ["read", "delete"], "approved_actions": ["read"]})[0]["issue"])

    def test_baseline_match(self):
        identity = {"granted_actions": ["read"], "approved_actions": ["read"],
                    "wildcard_resource": False, "unused_days": 1, "human_user": False}
        self.assertEqual([], audit(identity))


if __name__ == "__main__":
    unittest.main()
