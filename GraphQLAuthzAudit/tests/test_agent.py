import unittest
from agent import audit


class GraphQLAuthzAuditTests(unittest.TestCase):
    def test_sensitive_field_requires_rule(self):
        self.assertIn("authorization", audit({"fields": [{"name": "account", "sensitive": True}]})[0]["issue"])

    def test_protected_schema(self):
        self.assertEqual([], audit({"fields": [{"name": "account", "sensitive": True,
                                                "authorization_rule": "owner", "mutation": False}]}))


if __name__ == "__main__":
    unittest.main()
