import unittest
from agent import audit


class ServiceAccountLeastPrivilegeAuditTests(unittest.TestCase):
    def test_wildcard_is_critical(self):
        self.assertEqual("critical", audit({"wildcard_permission": True})[0]["severity"])

    def test_only_required_permissions_is_clean(self):
        self.assertEqual([], audit({"granted_permissions": ["read"], "required_permissions": ["read"],
                                    "workload_identity": True, "days_since_last_use": 2}))


if __name__ == "__main__":
    unittest.main()
