import unittest
from agent import audit


class WebAppCORSWildcardAuditTests(unittest.TestCase):

    def test_wildcard_with_credentials(self):
        self.assertTrue(audit({"cors_allow_origin": "*", "cors_allow_credentials": True}))

    def test_ok(self):
        self.assertFalse(audit({"cors_allow_origin": "https://app.example.com", "cors_allow_credentials": True, "serves_sensitive_data": True}))
