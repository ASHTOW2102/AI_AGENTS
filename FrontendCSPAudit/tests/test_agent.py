import unittest
from agent import audit


class FrontendCSPAuditTests(unittest.TestCase):
    def test_unsafe_inline_in_production(self):
        self.assertTrue(any("unsafe-inline" in f["issue"] for f in audit({"production": True, "unsafe_inline": True})))

    def test_restrictive_policy(self):
        policy = {"production": True, "directives": {"default-src": ["'self'"]},
                  "unsafe_inline": False, "wildcard_sources": False, "reporting_configured": True}
        self.assertEqual([], audit(policy))


if __name__ == "__main__":
    unittest.main()
