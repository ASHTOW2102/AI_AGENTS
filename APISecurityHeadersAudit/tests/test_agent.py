import unittest
from agent import audit


class APISecurityHeadersAuditTests(unittest.TestCase):
    def test_missing_header(self):
        self.assertIn("X-Content-Type-Options", audit({"required_headers": ["X-Content-Type-Options"]})[0]["issue"])

    def test_compliant_response(self):
        site = {"required_headers": ["X-Frame-Options"], "present_headers": ["X-Frame-Options"],
                "production": True, "server_version_disclosed": False, "referrer_policy": "strict-origin"}
        self.assertEqual([], audit(site))


if __name__ == "__main__":
    unittest.main()
