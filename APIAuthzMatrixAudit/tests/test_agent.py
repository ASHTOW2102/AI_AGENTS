import unittest
from agent import audit


class APIAuthzMatrixAuditTests(unittest.TestCase):
    def test_sensitive_route_without_policy(self):
        self.assertIn("authorization policy", audit({"routes": [{"name": "billing", "sensitive_operation": True}]})[0]["issue"])

    def test_protected_routes(self):
        data = {"routes": [{"name": "profile", "authenticated_required": True,
                            "auth_middleware": True, "authorization_policy": "owner"}]}
        self.assertEqual([], audit(data))


if __name__ == "__main__":
    unittest.main()
