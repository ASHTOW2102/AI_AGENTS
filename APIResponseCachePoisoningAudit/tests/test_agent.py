import unittest
from agent import audit


class APIResponseCachePoisoningAuditTests(unittest.TestCase):

    def test_unkeyed_header(self):
        self.assertTrue(audit({"response_varying_headers": ["X-Forwarded-Host"], "cache_key_headers": []}))

    def test_ok(self):
        self.assertFalse(audit({"response_varying_headers": ["Accept"], "cache_key_headers": ["Accept"], "cached": True, "cache_key_includes_auth_scope": True}))
